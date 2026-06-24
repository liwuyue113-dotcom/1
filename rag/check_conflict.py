import argparse

from rag.conflict_checker import check_setting_conflict, format_conflict_result
from rag.embedding_service import encode_texts, load_embedding_model
from rag.rag_config import CHUNKS_PATH, EMBEDDINGS_PATH, MIN_SIMILARITY, TOP_K
from rag.vector_store import load_index, search_vectors


def check_candidate_setting(candidate_setting: str) -> dict:
    chunks, embeddings = load_index(CHUNKS_PATH, EMBEDDINGS_PATH)
    model = load_embedding_model()
    query_embedding = encode_texts(model, [candidate_setting])[0]
    matches = search_vectors(
        query_embedding,
        embeddings,
        chunks,
        top_k=TOP_K,
    )
    return check_setting_conflict(
        candidate_setting,
        matches,
        min_similarity=MIN_SIMILARITY,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="检查新增设定是否可能与 RAG 已确认设定冲突。")
    parser.add_argument("candidate_setting", nargs="?", help="要检查的新增设定文本")
    args = parser.parse_args()

    candidate_setting = args.candidate_setting or input("新增设定：").strip()
    if not candidate_setting:
        print("未输入新增设定。")
        return

    result = check_candidate_setting(candidate_setting)
    print(format_conflict_result(result))


if __name__ == "__main__":
    main()
