import numpy as np

# In-memory storage for vectors and their corresponding texts
vectors = None
texts = []


def add(new_texts: list[str], new_vectors):
    """Store texts and their vector representations."""
    global vectors, texts
    texts = new_texts
    vectors = new_vectors


def cosine_similarity(query, stored_vectors):
    """Calculate similarity between query vector and all stored vectors."""
    query_norm = query / np.linalg.norm(query)
    vectors_norm = stored_vectors / np.linalg.norm(stored_vectors, axis=1, keepdims=True)
    return np.dot(vectors_norm, query_norm)


def search(query_vector, top_k: int = 3):
    """Find the top_k most similar passages to the query vector."""
    if vectors is None:
        return []

    scores = cosine_similarity(query_vector, vectors)
    top_indices = np.argsort(scores)[::-1][:top_k]

    return [
        {"text": texts[i], "score": float(scores[i])}
        for i in top_indices
    ]
