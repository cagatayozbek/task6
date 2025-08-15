import gradio as gr
import requests

API_URL = "http://127.0.0.1:8000/search"

def search_api(query, top_k=5):
    response = requests.post(API_URL, json={"query": query, "top_k": top_k})
    if response.status_code == 200:
        results = response.json()["results"]
        return "\n\n---\n\n".join([
            f"""<div style='padding: 10px; border: 1px solid #444; border-radius: 8px; margin-bottom: 12px; background-color: #1e1e1e'>
<b>🔹 Title:</b> <a href="{r['source']}" target="_blank">{r['title']}</a><br>
<b>📄 Score:</b> <code>{r['score']:.4f}</code><br>
<p style='margin-top: 5px; font-size: 14px; color: #ddd'>{r['text']}</p>
</div>
""" for r in results
        ])
    else:
        return "<span style='color:red;'>❌ API'den cevap alınamadı.</span>"

with gr.Blocks(css=".gr-box { background-color: #111 !important; }") as demo:
    gr.Markdown("""
# 🔍 <span style='color:#f97316'>Semantic Search App</span>

Wikipedia tabanlı semantik arama sistemi.  

""")

    with gr.Row():
        with gr.Column():
            query = gr.Textbox(label="📝 Sorgu", placeholder="örneğin: amino asit çeşitleri nelerdir", lines=2)
            submit_btn = gr.Button("🔎 Ara", elem_id="submit-btn")

    output = gr.Markdown()

    submit_btn.click(fn=search_api, inputs=query, outputs=output)

if __name__ == "__main__":
    demo.launch()