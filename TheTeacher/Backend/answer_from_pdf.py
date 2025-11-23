
from RAG_answer import answer_question
from dotenv import load_dotenv
import os

from google import genai

load_dotenv()  # Loads variables from .env

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

def answer_from_pdf(filepath, question):

    rag_answer = answer_question(file_path, question)

    query = \
        f"""Consider the following Data : {rag_answer}. Answer this question : {question}"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=query,
    )

    return response.text

#print(answer_from_pdf(r"C:\Users\pokhr\OneDrive\Desktop\Current_elecf.pdf", "What is Life?"))

