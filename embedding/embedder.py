from sentence_transformers import SentenceTransformer
import torch

class Embedder:
    def __init__(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = SentenceTransformer(
            "intfloat/multilingual-e5-large",
            device=device
        )

    def embed(self, texts):
        return self.model.encode(
            texts,
            normalize_embeddings=True,
            show_progress_bar=True
        )
