from sentence_transformers import SentenceTransformer

# Load model once at module level to avoid reloading on each call
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embeddings(texts: list[str]):
    """Convert list of texts into vector representations."""
    return model.encode(texts, convert_to_numpy=True)
