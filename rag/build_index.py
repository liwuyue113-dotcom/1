from rag.document_loader import load_markdown_chunks
from rag.embedding_service import build_embedding_text, encode_texts, load_embedding_model
from rag.rag_config import (
    CHUNKS_PATH,
    EMBEDDINGS_PATH,
    PROJECT_ROOT,
    SOURCE_FILES,
)
from rag.vector_store import save_index


def main() -> None:
    chunks = load_markdown_chunks(PROJECT_ROOT, SOURCE_FILES)
    model = load_embedding_model()
    embeddings = encode_texts(model, [build_embedding_text(chunk) for chunk in chunks])
    save_index(chunks, embeddings, CHUNKS_PATH, EMBEDDINGS_PATH)
    print(f"索引构建完成，共写入 {len(chunks)} 个设定片段。")


if __name__ == "__main__":
    main()
