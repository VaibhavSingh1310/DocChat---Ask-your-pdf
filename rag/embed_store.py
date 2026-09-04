import numpy as np
import faiss
from sentence_transformers import SentenceTransformer


class VectorStore:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.chunks: list[str] = []

    def build(self, chunks: list[str]) -> None:
        self.chunks = chunks
        embeddings = self.model.encode(chunks)
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(np.array(embeddings).astype("float32"))

    def search(self, query: str, k: int = 3) -> list[str]:
        if self.index is None:
            raise ValueError("Index not built yet. Call build() first.")
        query_vec = self.model.encode([query]).astype("float32")
        _, idx = self.index.search(query_vec, k)
        return [self.chunks[i] for i in idx[0]]
