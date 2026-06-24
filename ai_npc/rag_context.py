from rag.answer_service import UNKNOWN_ANSWER, answer_question
from rag.rag_config import (
    CHUNKS_PATH,
    EMBEDDINGS_PATH,
    MIN_SIMILARITY,
    TOP_K,
)


def build_npc_rag_query(player_message: str, npc_name: str = "胆小守卫") -> str:
    message = player_message.strip()
    return "\n".join(
        [
            "《囚城营救》AI NPC 世界观问答检索",
            f"NPC：{npc_name}",
            f"玩家问题：{message}",
            "检索重点：世界观、角色、地点、任务、路线、胆小守卫、姬野、吕归尘、离国边境城堡。",
        ]
    )


def format_npc_rag_context(matches: list[dict]) -> str:
    if not matches:
        return ""

    lines = ["NPC RAG 设定依据："]
    for index, match in enumerate(matches, start=1):
        source = match.get("source", "")
        heading = match.get("heading", "")
        text = match.get("text", "").strip()
        score = match.get("score")
        score_text = f" 相似度：{score:.3f}" if isinstance(score, float) else ""
        lines.append(f"{index}. 来源：{source} / {heading}{score_text}")
        lines.append(f"   内容：{text}")
    return "\n".join(lines)


def answer_npc_world_question(
    player_message: str,
    matches: list[dict],
    min_similarity: float = MIN_SIMILARITY,
    api_key: str | None = None,
) -> dict:
    result = answer_question(
        player_message,
        matches,
        min_similarity=min_similarity,
        api_key=api_key,
    )
    used_rag = bool(result["sources"]) and result["answer"] != UNKNOWN_ANSWER

    return {
        "reply": result["answer"],
        "sources": result["sources"],
        "matches": result["matches"],
        "used_rag": used_rag,
        "rag_context": format_npc_rag_context(result["matches"]) if used_rag else "",
    }


def retrieve_npc_rag_matches(player_message: str, top_k: int = TOP_K) -> list[dict]:
    from rag.embedding_service import encode_texts, load_embedding_model
    from rag.vector_store import load_index, search_vectors

    chunks, embeddings = load_index(CHUNKS_PATH, EMBEDDINGS_PATH)
    model = load_embedding_model()
    query = build_npc_rag_query(player_message)
    query_embedding = encode_texts(model, [query])[0]
    return search_vectors(query_embedding, embeddings, chunks, top_k=top_k)


def answer_npc_with_rag(
    player_message: str,
    api_key: str | None = None,
    min_similarity: float = MIN_SIMILARITY,
) -> dict:
    try:
        matches = retrieve_npc_rag_matches(player_message)
    except Exception as error:
        return {
            "reply": UNKNOWN_ANSWER,
            "sources": [],
            "matches": [],
            "used_rag": False,
            "rag_context": "",
            "warning": f"未能读取 RAG 索引：{error}",
        }

    return answer_npc_world_question(
        player_message,
        matches,
        min_similarity=min_similarity,
        api_key=api_key,
    )
