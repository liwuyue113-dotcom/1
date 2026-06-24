import json
from pathlib import Path

import numpy as np


def search_vectors(
    query_embedding: np.ndarray,
    embeddings: np.ndarray,
    chunks: list[dict],
    top_k: int = 3,
) -> list[dict]:
    if len(embeddings) != len(chunks):
        raise ValueError("向量数量与文本片段数量不一致")

    query = np.asarray(query_embedding, dtype=float)
    matrix = np.asarray(embeddings, dtype=float)

    query_norm = np.linalg.norm(query)
    row_norms = np.linalg.norm(matrix, axis=1)
    denominator = row_norms * query_norm
    scores = np.divide(
        matrix @ query,
        denominator,
        out=np.zeros_like(row_norms, dtype=float),
        where=denominator != 0,
    )

    result_count = min(top_k, len(chunks))
    indexes = np.argsort(scores)[::-1][:result_count]

    return [
        {
            **chunks[index],
            "score": float(scores[index]),
        }
        for index in indexes
    ]


def save_index(
    chunks: list[dict],
    embeddings: np.ndarray,
    chunks_path: Path,
    embeddings_path: Path,
) -> None:
    chunks_path.parent.mkdir(parents=True, exist_ok=True)
    chunks_path.write_text(
        json.dumps(chunks, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    np.save(embeddings_path, embeddings)


def load_index(chunks_path: Path, embeddings_path: Path) -> tuple[list[dict], np.ndarray]:
    if not chunks_path.exists() or not embeddings_path.exists():
        raise FileNotFoundError("找不到 RAG 索引，请先运行 python -m rag.build_index")

    chunks = json.loads(chunks_path.read_text(encoding="utf-8"))
    embeddings = np.load(embeddings_path)
    return chunks, embeddings
