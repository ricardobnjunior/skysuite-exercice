# AI-Powered Document Q&A System

A lightweight RAG (Retrieval-Augmented Generation) system for answering questions based on document text.

## Setup

```bash
# Create and activate conda environment
conda create -n skysuite python=3.11 -y
conda activate skysuite

# Install dependencies
pip install -r requirements.txt
```

## Testing Each Part

### Part 1: Retrieval System

Tests the semantic search using embeddings and cosine similarity. No LLM required.

```bash
python part1_retrieval.py
```

Expected output:
```
Question: What's the average rent per square foot?

Relevant passages:

1. [Score: 0.7490]
   The average rent per square foot in the downtown area is $45.00...

2. [Score: 0.6341]
   Monthly operating expenses average $12.50 per square foot...
```

### Part 2: RAG with LLM

Tests the full pipeline: retrieval + LLM-generated answer.

Requires `.env` file with:
```
OPENROUTER_API_KEY=your-api-key
```

```bash
python part2_with_llm.py
```

Expected output:
```
Question: What's the average rent per square foot?

Retrieved passages:
  1. [Score: 0.7490] The average rent per square foot...

--------------------------------------------------

LLM Answer:
The average rent per square foot is $45.00 for commercial properties.
```

### Part 3: Design Document

No code to run. See [DESIGN.md](DESIGN.md) for architectural decisions.

## Project Structure

```
├── part1_retrieval.py   # Test Part 1 (retrieval only)
├── part2_with_llm.py    # Test Part 2 (retrieval + LLM)
├── DESIGN.md            # Part 3 (design reasoning)
├── requirements.txt
├── .env                 # API key (not committed)
├── data/
│   └── sample_passages.txt
└── src/
    ├── embeddings.py    # Embedding generation
    ├── vector_store.py  # In-memory vector storage
    ├── retriever.py     # Retrieval orchestration
    └── llm.py           # LLM integration
```

## Changing the Query

Edit the `query` variable in `part1_retrieval.py` or `part2_with_llm.py`:

```python
query = "How many parking spaces are available?"
```
