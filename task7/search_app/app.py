from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from utils.embeddings import encode_query
from utils.data_loader import load_chunks, load_faiss_index
from utils.faiss_search import search_faiss

app = FastAPI(title="Semantic Search API")

# Veri ve index'i başta yükleyelim (cache)
chunks = load_chunks()
index = load_faiss_index()

class SearchRequest(BaseModel):
    query: str
    top_k: int = 5

@app.post("/search")
def search(request: SearchRequest):
    query_embedding = encode_query(request.query)
    results = search_faiss(query_embedding, index, chunks, top_k=request.top_k)
    return {
        "query": request.query,
        "results": results
    }