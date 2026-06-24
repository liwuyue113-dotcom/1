from dataclasses import dataclass


@dataclass
class LevelDesignInput:
    theme: str
    player_goal: str
    difficulty: str
    route_notes: str
    rag_context: str = ""


def generate_level_plan(design_input: LevelDesignInput) -> str:
    _validate_input(design_input)

    theme = design_input.theme.strip()
    player_goal = design_input.player_goal.strip()
    difficulty = design_input.difficulty.strip()
    route_notes = design_input.route_notes.strip()

    lines = [
        f"# {theme}关卡策划案",
        "",
        "## 玩家目标",
        f"- 目标：{player_goal}",
        f"- 难度：{difficulty}",
        "",
        "## 三条路线设计",
        "### 上路",
        "- 定位：正常路线，路线较长，敌人数量一般。",
        "- 玩法重点：前段让玩家逐个观察守卫，后段用连续站岗制造压力。",
        "",
        "### 中路",
        "- 定位：正常路线，长度一般，敌人略多。",
        "- 玩法重点：用更密集的守卫站位提高正面压力。",
        "",
        "### 下方暗道",
        "- 定位：隐藏路线，长度正常，敌人最少。",
        "- 玩法重点：需要胆小守卫真实情报才能明确入口方向。",
        "",
        "## 敌人配置",
        "- 上路：开始分散，后段出现连续几个守卫站岗。",
        "- 中路：敌人分布更多，部分位置有多个守卫站岗。",
        "- 下方暗道：暗道内部只有一个站岗守卫。",
        "",
        "## 风险与奖励",
        "- 上路风险来自时间消耗，奖励是敌人压力相对稳定。",
        "- 中路风险来自敌人密度，奖励是路线长度适中。",
        "- 下方暗道风险来自入口信息不明显，奖励是敌人最少。",
        "",
        "## 失败条件",
        "- 倒计时结束前没有找到吕归尘。",
        "- 玩家在高压路线上被守卫持续阻拦，导致时间不足。",
        "",
        "## 设计意图",
        "- 让玩家在时间、敌人压力和情报收益之间做路线选择。",
        "- 让胆小守卫的真实情报影响实际路线判断，而不是只提供剧情文本。",
    ]

    rag_context = design_input.rag_context.strip()
    if rag_context:
        lines.extend(["", "## RAG 设定依据", rag_context])

    lines.extend(
        [
            "",
            "## 优化建议",
            f"- 根据实际 Unity 场景检查路线设定：{route_notes}",
        ]
    )

    return "\n".join(lines)


def _validate_input(design_input: LevelDesignInput) -> None:
    required_fields = {
        "theme": design_input.theme,
        "player_goal": design_input.player_goal,
        "difficulty": design_input.difficulty,
        "route_notes": design_input.route_notes,
    }
    for field_name, value in required_fields.items():
        if not value or not value.strip():
            raise ValueError(f"{field_name} is required")
