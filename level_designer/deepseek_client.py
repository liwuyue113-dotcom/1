import json
import urllib.error
import urllib.request

from level_designer.generator import LevelDesignInput


DEFAULT_DEEPSEEK_URL = "https://api.deepseek.com/chat/completions"
DEFAULT_DEEPSEEK_MODEL = "deepseek-chat"


class DeepSeekError(RuntimeError):
    pass


class DeepSeekClient:
    def __init__(
        self,
        api_key: str,
        model: str = DEFAULT_DEEPSEEK_MODEL,
        base_url: str = DEFAULT_DEEPSEEK_URL,
        timeout: int = 60,
    ):
        if not api_key or not api_key.strip():
            raise ValueError("api_key is required")
        self.api_key = api_key.strip()
        self.model = model
        self.base_url = base_url
        self.timeout = timeout

    def generate(self, prompt: str) -> str:
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": "你是游戏关卡策划助手，只输出中文 Markdown 关卡策划案。",
                },
                {"role": "user", "content": prompt},
            ],
            "temperature": 0.7,
        }
        request = urllib.request.Request(
            self.base_url,
            data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )

        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                response_data = json.loads(response.read().decode("utf-8"))
        except urllib.error.URLError as exc:
            raise DeepSeekError(f"DeepSeek request failed: {exc}") from exc
        except json.JSONDecodeError as exc:
            raise DeepSeekError("DeepSeek returned invalid JSON") from exc

        try:
            content = response_data["choices"][0]["message"]["content"]
        except (KeyError, IndexError, TypeError) as exc:
            raise DeepSeekError("DeepSeek response missing message content") from exc

        if not content or not content.strip():
            raise DeepSeekError("DeepSeek returned empty content")
        return content.strip()


def build_level_design_prompt(design_input: LevelDesignInput) -> str:
    lines = [
        "请基于下面输入，生成一份《囚城营救》的关卡策划案。",
        "",
        f"关卡主题：{design_input.theme.strip()}",
        f"玩家目标：{design_input.player_goal.strip()}",
        f"难度：{design_input.difficulty.strip()}",
        f"三条路线资料：{design_input.route_notes.strip()}",
    ]

    rag_context = design_input.rag_context.strip()
    if rag_context:
        lines.extend(
            [
                "",
                "以下是 RAG 从已确认设定中检索到的依据，优先遵守，不要编造冲突信息：",
                rag_context,
            ]
        )

    lines.extend(
        [
            "",
            "必须使用下面 Markdown 栏目，不要新增大系统设定：",
            f"# {design_input.theme.strip()}关卡策划案",
            "## 玩家目标",
            "## 三条路线设计",
            "### 上路",
            "### 中路",
            "### 下方暗道",
            "## 敌人配置",
            "## 风险与奖励",
            "## 失败条件",
            "## 设计意图",
            "## 优化建议",
        ]
    )
    return "\n".join(lines)


def generate_plan_with_deepseek(design_input: LevelDesignInput, client: DeepSeekClient) -> str:
    prompt = build_level_design_prompt(design_input)
    return client.generate(prompt)
