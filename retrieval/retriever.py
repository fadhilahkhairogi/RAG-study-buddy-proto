from sentence_transformers import CrossEncoder
import torch

class Retriever:
    def __init__(self, store, embedder):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        self.store = store
        self.embedder = embedder
        self.reranker = CrossEncoder(
            "cross-encoder/ms-marco-MiniLM-L-6-v2",
            device=device
        )
        
    def retrieve(self, query):
        q_vec = self.embedder.embed([query])[0]
        raw = self.store.search(q_vec)

        chunks = [
            r["text"]
            for r in raw["data"]["Get"]["Chunk"]
        ]

        scores = self.reranker.predict(
            [[query, c] for c in chunks]
        )

        ranked = sorted(zip(chunks, scores), key=lambda x: x[1], reverse=True)
        return [c for c, _ in ranked[:5]]
