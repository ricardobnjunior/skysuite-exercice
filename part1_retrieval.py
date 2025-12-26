"""Part 1: Minimal Retrieval System - Semantic search without LLM"""

from pathlib import Path
from src import retriever

data_file = Path(__file__).parent / "data" / "sample_passages.txt"
retriever.index_from_file(str(data_file))

query = "What's the average rent per square foot?"
results = retriever.retrieve(query, top_k=3)

print(f"Question: {query}\n")
print("Relevant passages:\n")
for i, result in enumerate(results, 1):
    print(f"{i}. [Score: {result['score']:.4f}]")
    print(f"   {result['text']}\n")
