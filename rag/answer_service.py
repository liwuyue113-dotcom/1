import os

UNKNOWN_ANSWER = "当前知识库没有足够信息。"
DEEPSEEK_URL = "https://api.deepseek.com/chat/completions"


def has_sufficient_evidence(matches: list[dict], min_similarity: float) -> bool:
    return bool(matches) and matches[0]["score"] >= min_similarity


def deduplicate_sources(matches: list[dict]) -> list[str]:
    sources = []
    for match in matches:
        source = match["source"]
        if source not in sources:
            sources.append(source)
    return sources


def build_grounded_prompt(question: str, matches: list[dict]) -> str:
    evidence_parts = []
    for index, match in enumerate(matches, start=1):
        evidence_parts.append(
            f"[片段 {index}]\n"
            f"来源：{match['source']}\n"
            f"标题：{match.get('heading', '')}\n"
            f"内容：{match['text']}"
        )

    evidence = "\n\n".join(evidence_parts)
    return (
        "你是《囚城营救》的游戏设定问答助手。\n"
        "只能根据提供的设定片段回答，不要补充片段中没有的信息。\n"
        f"如果片段无法回答问题，请回答“{UNKNOWN_ANSWER}”\n"
        "回答保持简短，不要在正文中伪造来源。\n\n"
        f"玩家问题：{question}\n\n"
        f"设定片段：\n{evidence}"
    )


def request_deepseek(prompt: str, api_key: str) -> str:
    try:
        import requests
    except ImportError as error:
        raise RuntimeError("缺少 requests，请先安装 rag/requirements.txt") from error

    response = requests.post(
        DEEPSEEK_URL,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": "deepseek-chat",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0,
        },
        timeout=30,
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()


def answer_question(
    question: str,
    matches: list[dict],
    min_similarity: float,
    api_key: str | None = None,
) -> dict:
    sources = deduplicate_sources(matches)

    if not has_sufficient_evidence(matches, min_similarity):
        return {
            "answer": UNKNOWN_ANSWER,
            "sources": [],
            "matches": matches,
        }

    if _contains_unconfirmed_marker(matches[0]["text"]):
        return {
            "answer": UNKNOWN_ANSWER,
            "sources": sources,
            "matches": matches,
        }

    prompt = build_grounded_prompt(question, matches)
    key = api_key or os.getenv("DEEPSEEK_API_KEY")

    if not key:
        answer = f"未调用 DeepSeek。最相关设定片段：{matches[0]['text']}"
    else:
        try:
            answer = request_deepseek(prompt, key)
        except Exception as error:
            answer = f"DeepSeek 调用失败（{error}）。最相关设定片段：{matches[0]['text']}"

    return {
        "answer": answer,
        "sources": sources,
        "matches": matches,
    }


def _contains_unconfirmed_marker(text: str) -> bool:
    markers = ["待补充", "尚待补充", "待确认", "尚未确认", "未知信息"]
    return any(marker in text for marker in markers)
