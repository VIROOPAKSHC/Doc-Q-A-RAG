# app.py
import gradio as gr
from src.rag_qa import rag_qa

iface = gr.Interface(
    fn=rag_qa,
    inputs="text",
    outputs="text",
    title="Document Q&A with LLaMA-2 RAG"
)

iface.launch()
