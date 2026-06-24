from level_designer.generator import LevelDesignInput


def build_rag_query(design_input: LevelDesignInput) -> str:
    return "\n".join(
        [
            "《囚城营救》三条路线关卡设定检索。",
            "重点检索：三条主路基础设定、路线长度、敌人数量、敌人站位、巡逻方式、路线提示方式。",
            "路线关键词：上路，中路，下方暗道，暗道路线，胆小守卫真实情报。",
            f"命令行路线资料：{design_input.route_notes.strip()}",
        ]
    )


def format_rag_matches(matches: list[dict]) -> str:
    if not matches:
        return ""

    lines = ["RAG 设定依据："]
    for index, match in enumerate(matches, start=1):
        source = match.get("source", "")
        heading = match.get("heading", "")
        text = match.get("text", "").strip()
        score = match.get("score")
        score_text = f" 相似度：{score:.3f}" if isinstance(score, float) else ""
        lines.append(f"{index}. 来源：{source} / {heading}{score_text}")
        lines.append(f"   内容：{text}")
    return "\n".join(lines)


def retrieve_rag_context(design_input: LevelDesignInput) -> str:
    try:
        from rag.embedding_service import encode_texts, load_embedding_model
        from rag.rag_config import CHUNKS_PATH, EMBEDDINGS_PATH, TOP_K
        from rag.vector_store import load_index, search_vectors

        chunks, embeddings = load_index(CHUNKS_PATH, EMBEDDINGS_PATH)
        model = load_embedding_model()
        query_embedding = encode_texts(model, [build_rag_query(design_input)])[0]
        matches = search_vectors(query_embedding, embeddings, chunks, top_k=TOP_K)
    except Exception as error:
        return f"RAG 设定依据：未能读取 RAG 索引，已使用命令行路线资料。原因：{error}"

    return format_rag_matches(matches)
