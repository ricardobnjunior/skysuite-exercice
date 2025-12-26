# Design Document - AI-Powered Document Q&A System

## Why Python for the AI Layer

- **Rich AI ecosystem**: Python has mature libraries for vector search (FAISS, ChromaDB), embeddings (sentence-transformers, OpenAI SDK), and LLM orchestration (LangChain). The C#/.NET ecosystem lacks equivalent tooling for these tasks.
- **Rapid prototyping**: Python allows faster iteration on AI features, which is critical when experimenting with different models, prompt strategies, and retrieval approaches.
- **Model compatibility**: Most pre-trained models (HuggingFace, OpenAI) provide first-class Python support with well-documented APIs.

## Integration with C#/.NET

- **REST API**: Expose the Python retrieval system as a lightweight HTTP service (Flask/FastAPI). The C# application calls this service when users submit questions. This is the simplest approach with minimal coupling.
- **Alternative options**: gRPC for better performance and type safety, or a message queue (RabbitMQ, Azure Service Bus) for async processing of document indexing tasks.

## Tradeoffs

- **Performance**: Python is slower than C# for CPU-bound tasks, but AI workloads are I/O-bound (API calls, model inference). The bottleneck is the LLM response time, not Python execution.
- **Maintainability**: Two languages increase complexity. Mitigate by keeping the Python service focused (only AI features) and using clear API contracts.
- **Integration cost**: Adding a Python microservice requires deployment infrastructure (Docker container, separate scaling). For SkySuite's use case, this overhead is justified by access to superior AI tooling.

## Production Considerations

- **Scaling**: For large document sets, replace in-memory vector store with a dedicated solution (Pinecone, Weaviate, or pgvector).
- **Context limits**: Chunk large documents and implement a re-ranking step to fit within LLM token limits.
- **Caching**: Cache embeddings for frequently accessed documents to reduce computation.
