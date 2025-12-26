from pathlib import Path
from . import embeddings, vector_store


def index_from_file(file_path: str):
    """Read passages from file and index them for search."""
    text = Path(file_path).read_text(encoding="utf-8")
    passages = [line.strip() for line in text.splitlines() if line.strip()]

    vectors = embeddings.generate_embeddings(passages)
    vector_store.add(passages, vectors)


def retrieve(query: str, top_k: int = 3):
    """Find most relevant passages for a given query."""
    query_vector = embeddings.generate_embeddings([query])[0]
    return vector_store.search(query_vector, top_k)
