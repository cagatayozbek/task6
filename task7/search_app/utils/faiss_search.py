import numpy as np
from typing import List, Dict, Any

def search_faiss(query_embedding: np.ndarray, index, chunks: List[Dict[str, Any]], top_k: int = 5):
    # Benzerlik skorlarını ve indexleri al
    scores, indices = index.search(query_embedding, top_k)

    # Eşleşen chunk'ları skorlarıyla birleştir
    results = []
    for score, idx in zip(scores[0], indices[0]):
        if idx == -1:
            continue  # eşleşme yoksa
        chunk = chunks[idx]
        results.append({
            "title": chunk.get("title", ""),
            "text": chunk.get("text", ""),
            "source": chunk.get("source", ""),
            "score": float(score)
        })

    return results