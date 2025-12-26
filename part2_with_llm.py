"""Part 2: RAG with LLM - Retrieval + AI-generated answer"""

from pathlib import Path
from src import retriever, llm

data_file = Path(__file__).parent / "data" / "sample_passages.txt"
retriever.index_from_file(str(data_file))

query = "What's the average rent per square foot?"
results = retriever.retrieve(query, top_k=3)

print(f"Question: {query}\n")
print("Retrieved passages:")
for i, result in enumerate(results, 1):
    print(f"  {i}. [Score: {result['score']:.4f}] {result['text']}")

print("\n" + "-" * 50)
print("\nLLM Answer:")
answer = llm.ask(query, results)
print(answer)
