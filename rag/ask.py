from rag.answer_service import answer_question
from rag.embedding_service import encode_texts, load_embedding_model
from rag.rag_config import (
    CHUNKS_PATH,
    EMBEDDINGS_PATH,
    MIN_SIMILARITY,
    TOP_K,
)
from rag.vector_store import load_index, search_vectors


def print_result(result: dict) -> None:
    print(f"\n回答：{result['answer']}")

    if result["sources"]:
        print("\n来源：")
        for source in result["sources"]:
            print(f"- {source}")

    if result["matches"]:
        print("\n检索片段：")
        for match in result["matches"]:
            print(
                f"- [{match['score']:.3f}] "
                f"{match['source']} / {match.get('heading', '')}"
            )


def main() -> None:
    chunks, embeddings = load_index(CHUNKS_PATH, EMBEDDINGS_PATH)
    model = load_embedding_model()

    print("《囚城营救》RAG 设定问答已启动。输入“退出”结束。")

    while True:
        question = input("\n问题：").strip()
        if question == "退出":
            break
        if not question:
            continue

        query_embedding = encode_texts(model, [question])[0]
        matches = search_vectors(
            query_embedding,
            embeddings,
            chunks,
            top_k=TOP_K,
        )
        result = answer_question(
            question,
            matches,
            min_similarity=MIN_SIMILARITY,
        )
        print_result(result)


if __name__ == "__main__":
    main()
