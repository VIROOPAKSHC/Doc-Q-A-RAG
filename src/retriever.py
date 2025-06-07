
import pickle
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
documents, filenames, faiss_index = pickle.load(open("index.pkl", "rb"))

def retrieve_top_k(query, k=3):
    q_embed = model.encode([query])
    D, I = faiss_index.search(q_embed, k)
    return [documents[i] for i in I[0]]
