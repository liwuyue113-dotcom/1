import hashlib

import numpy as np

from rag.rag_config import EMBEDDING_MODEL_NAME


class LocalTextEmbeddingModel:
    def __init__(self, dimensions: int = 2048):
        self.dimensions = dimensions

    def encode(self, texts: list[str], normalize_embeddings: bool = True):
        vectors = np.zeros((len(texts), self.dimensions), dtype=float)

        for row, text in enumerate(texts):
            compact = "".join(text.lower().split())
            features = list(compact)
            features.extend(compact[index : index + 2] for index in range(len(compact) - 1))

            for feature in features:
                digest = hashlib.blake2b(feature.encode("utf-8"), digest_size=8).digest()
                column = int.from_bytes(digest, "little") % self.dimensions
                vectors[row, column] += 1.0

            if normalize_embeddings:
                norm = np.linalg.norm(vectors[row])
                if norm:
                    vectors[row] /= norm

        return vectors


def build_embedding_text(chunk: dict) -> str:
    heading = chunk.get("heading", "").strip()
    text = chunk["text"].strip()

    if not heading:
        return text

    return f"{heading}：{text}"


def load_embedding_model():
    try:
        from sentence_transformers import SentenceTransformer
    except Exception:
        print("未加载 sentence-transformers，使用内置本地文本向量兜底。")
        return LocalTextEmbeddingModel()

    return SentenceTransformer(EMBEDDING_MODEL_NAME)


def encode_texts(model, texts: list[str]):
    return model.encode(texts, normalize_embeddings=True)
