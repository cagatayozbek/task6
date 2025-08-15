# 🔍 Semantic Search App

A semantic vector-based search engine built on **Wikipedia data**.  
This app allows you to ask natural language questions and retrieve **semantically similar content**.

## 🚀 Features

- 🧠 Text embeddings with `SentenceTransformer`
- ⚡ Fast vector similarity search using `FAISS`
- 📊 Score-based ranking (Dot Product / Cosine Similarity)
- 🌐 REST API powered by `FastAPI`
- 🎨 Modern UI built with `Gradio`
- 🔗 Wikipedia titles and source URLs

---

## 📁 Project Structure

```
search_app/
├── app.py                     # FastAPI backend
├── ui_gradio.py              # Gradio frontend
├── requirements.txt
├── data/
│   ├── chunks.json           # Chunked Wikipedia content
│   └── faiss_index.bin       # FAISS vector index
└── utils/
    ├── embeddings.py         # Embedding logic
    ├── faiss_search.py       # FAISS search functions
    └── data_loader.py        # Load data and index
```

---

## ⚙️ Setup

### 1. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

> Includes `sentence-transformers`, `faiss-cpu`, `fastapi`, `uvicorn`, `gradio`, and more.

---

## ▶️ Run the App

### 1. Start the API Server
```bash
python app.py
# or
uvicorn app:app --reload
```

### 2. Launch Gradio UI
```bash
python ui_gradio.py
```

Then visit 👉 http://127.0.0.1:7860 in your browser.

---

## 🧪 Example Queries

- `"what are types of amino acids"`
- `"who is ajax"`
- `"contributions of ada lovelace"`
- `"what happened on april 11"`

---

## 🧠 Notes

- Embeddings are normalized for cosine similarity with FAISS dot product.
- Example `chunks.json` format:
```json
{
  "title": "Amino acid",
  "text": "...",
  "source": "https://en.wikipedia.org/wiki/Amino%20acid"
}
```
- You can extend this app with recall@k, adversarial queries, BM25 comparisons, etc.

---

## 📄 License

MIT License – free to use and modify.

---
