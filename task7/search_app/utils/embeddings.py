from sentence_transformers import SentenceTransformer
import numpy as np

# Modeli sadece 1 kez yükleyelim
_model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

def encode_query(query: str) -> np.ndarray:
    embedding = _model.encode(
        query,
        normalize_embeddings=True,  # cosine similarity için
        show_progress_bar=False
    )
    return embedding.reshape(1, -1)  # FAISS için 2D array