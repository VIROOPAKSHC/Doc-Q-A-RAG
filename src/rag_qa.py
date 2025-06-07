from .retriever import retrieve_top_k
from .generator import generate_answer

def rag_qa(query):
    context_chunks = retrieve_top_k(query)
    context = "\n".join(context_chunks)
    answer = generate_answer(context, query)
    return answer
