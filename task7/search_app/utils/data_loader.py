import json
import faiss
import os

# Dosya yolları
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CHUNKS_PATH = os.path.join(BASE_DIR, "data", "chunks.json")
INDEX_PATH = os.path.join(BASE_DIR, "data", "faiss_index.bin")

# chunks.json yükle
def load_chunks():
    with open(CHUNKS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

# FAISS index yükle
def load_faiss_index():
    return faiss.read_index(INDEX_PATH)