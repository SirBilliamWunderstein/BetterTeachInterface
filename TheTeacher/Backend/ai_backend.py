from google import genai

from chunk_extractor import chunk_extractor
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import numpy as np
import faiss
import os


load_dotenv()  # Loads variables from .env

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


class AIBackend:

    def __init__(self, filepath=None):

        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.filepath = filepath

        text_and_chunks = chunk_extractor(self.filepath)
        self.text = text_and_chunks[0].strip("*")
        self.chunks = text_and_chunks[1]

        self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

        self.embeddings = self.model.encode(self.chunks)
        self.embeddings = np.array(self.embeddings).astype("float32")

        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(self.embeddings)

    def answer_general_query(self, query):

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=query,
        )

        return response.text

    def answer_from_pdf (self, query, k=1) :

        query_emb = self.model.encode([query]).astype("float32")

        distances, indexes = self.index.search(query_emb, k)

        results = []
        for i, idx in enumerate(indexes[0]):
            results.append({
                "chunk": self.chunks[idx],
                "distance": float(distances[0][i])
            })

        answers = [result["chunk"] for result in results]
        string_answer = ""

        for answer in answers:
            string_answer += answer

        answer = string_answer

        query = \
            f"""Consider the following Data : {answer}. Answer this question : {query}"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=query,
        )

        return response.text;

    def ask_from_pdf (self) :
        query = \
            f"""Generate 10 questions from the following text so as to test knowledge as well as understanding. 
            Start from easy questions then move onto the conceptual ones. Only generate questions and nothing else. Seperate questions by | character
\n\n {self.text}"""


        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=query,
        )

        return response.text




backend = AIBackend(r"C:\Users\pokhr\OneDrive\Desktop\Current_elecf.pdf")

#questions = AIBackend.ask_from_pdf().split("|")

