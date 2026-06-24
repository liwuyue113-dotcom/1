from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

SOURCE_FILES = [
    "docs/rag_setting.md",
]

DATA_DIR = Path(__file__).resolve().parent / "rag_data"
CHUNKS_PATH = DATA_DIR / "chunks.json"
EMBEDDINGS_PATH = DATA_DIR / "embeddings.npy"

EMBEDDING_MODEL_NAME = "BAAI/bge-small-zh-v1.5"
TOP_K = 3
MIN_SIMILARITY = 0.35
