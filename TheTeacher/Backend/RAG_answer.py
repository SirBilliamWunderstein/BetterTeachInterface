from sentence_transformers import SentenceTransformer
from BetterTeachInterface.TheTeacher.Backend.chunk_extractor import chunk_extractor
import numpy as np
import faiss

# from google import genai
# from dotenv import load_dotenv
# import os
#
# load_dotenv()  # Loads variables from .env
#
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


#client = genai.Client(api_key=GEMINI_API_KEY)

def answer_question (filepath, question) :

    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    chunks = chunk_extractor(filepath)


    embeddings = model.encode(chunks)
    embeddings = np.array(embeddings).astype("float32")


    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)


    def search(query, k):
        query_emb = model.encode([query]).astype("float32")

        distances, indexes = index.search(query_emb, k)


        results = []
        print(indexes)
        print(indexes[0])
        for i, idx in enumerate(indexes[0]):
            results.append({
                "chunk": chunks[idx],
                "distance": float(distances[0][i])
            })

        return results


    res = search(question, k=3)
    answer = res[0]["chunk"]

    return answer



print(answer_question(r"C:\Users\pokhr\OneDrive\Desktop\Current_elecf.pdf", input("Enter Question : ")))

