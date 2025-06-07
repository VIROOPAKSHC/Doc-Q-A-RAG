# 📄 Doc‑Q‑A‑RAG

**Doc-Q-A-RAG** is a modular **Retrieval‑Augmented Generation (RAG)** pipeline for intelligent question-answering over documents. It leverages vector embeddings, semantic search, and powerful LLMs like GPT‑4 to produce context-aware, accurate responses directly sourced from the document contents.

> ⚠️ **Note:** This project is currently **in active development**. Core components are being built and tested, and contributions or suggestions are welcome!

---

## 🚀 Features

- **📚 Multi-format Document Input** — Supports ingestion of PDF, TXT, DOCX files (planned).
- **🔍 Chunking + Embeddings** — Splits documents into semantically useful chunks and embeds them using OpenAI embeddings (or HuggingFace).
- **⚡ Vector Search (FAISS)** — Fast and scalable similarity search using dense vector indexes.
- **🧠 LLM-Driven Answers** — Uses GPT models to synthesize answers from retrieved content.
- **💾 (Optional) Caching** — Support for caching previously answered queries to reduce latency.
- **🧪 Modular & Extensible** — Easy to swap in custom retrievers, chunkers, or LLMs.

---

## 📦 Project Status

| Component            | Status         |
|----------------------|----------------|
| Document Ingestion   | ✅ Basic support for TXT/PDF |
| Embedding Generator  | ✅ Working with OpenAI Embeddings |
| Vector Store (FAISS) | ✅ Integrated |
| Question Answering   | ✅ Basic GPT-3.5/4 Support |
| Web/CLI Interface    | 🚧 In Progress |
| Chunking Improvements| 🚧 Being optimized |
| Evaluation Pipeline  | ⏳ Planned |
| LangChain Support    | ⏳ Exploring |
| LLM Models           | ⏳ Exploring |
| Dataset Expansion    | ⏳ Exploring |
---

## 🛠️ Installation

### 🔧 Prerequisites

- Python 3.8+
- `faiss-cpu` or `faiss-gpu`
- OpenAI API key

### 🧩 Setup

```bash
git clone https://github.com/VIROOPAKSHC/Doc-Q-A-RAG.git
cd Doc-Q-A-RAG
python3 -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create a .env file:
```ini
OPENAI_API_KEY=your_openai_key_here
```

### ⚙️ Usage

#### 📝 Document Indexing
```bash
python app.py --docs path/to/docs/*.pdf
```

#### ❓ Ask Questions
```bash
python qa.py --query "What are the steps in the RAG pipeline?"
```
You’ll get an answer generated from the most relevant parts of the ingested documents.

### 📁 Project Structure

```text
Doc-Q-A-RAG/
├── app.py              # Ingest and embed documents
├── qa.py               # Query interface
├── retriever.py        # FAISS-based vector search
├── embeddings.py       # OpenAI/HF embedding utilities
├── chunker.py          # Document chunking logic
├── cache.py            # Optional caching module
├── requirements.txt    # Python dependencies
└── README.md           # You're reading it :)
```

### 🧠 Acknowledgments
- [RAG: Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401)
- [FAISS by Facebook AI](https://github.com/facebookresearch/faiss)
- [LangChain](https://github.com/hwchase17/langchain)
- [LlamaIndex](https://github.com/jerryjliu/llama_index)

### 👤 Author
Viroopaksh C
AI/ML Researcher & Engineer
[🔗 LinkedIn](https://www.linkedin.com/in/viroopaksh-chekuri) | ✉️ Open to collaboration!
