from sentence_transformers import SentenceTransformer
import faiss, os, pickle

model = SentenceTransformer('all-MiniLM-L6-v2') 

documents = []
filenames = []

for fname in os.listdir('data/'):
    with open(f'data/{fname}', 'r', encoding='utf-8') as f:
        text = f.read()
        chunks = [text[i:i+500] for i in range(0, len(text), 500)]
        documents.extend(chunks)
        filenames.extend([fname]*len(chunks))

embeddings = model.encode(documents, show_progress_bar=True)
faiss_index = faiss.IndexFlatL2(embeddings.shape[1])
faiss_index.add(embeddings)

pickle.dump((documents, filenames, faiss_index), open("index.pkl", "wb"))


