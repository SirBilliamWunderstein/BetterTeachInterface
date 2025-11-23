
from pdf_to_text import text_extractor

pdf = r"C:\Users\pokhr\OneDrive\Desktop\Current_elecf.pdf"

def chunk_extractor(filepath):

    text_s = text_extractor(pdf)
    text = text_s.split()



    chunk_size = 300
    overlap = 150
    pointer = 0


    chunks = [text[pointer-overlap: pointer+chunk_size+overlap] for pointer in range(0, len(text), chunk_size)]
    string_chunks = []

    string_chunk = ""

    for list_chunk in chunks:
        for string in list_chunk:
            string_chunk += string + " "

        string_chunks.append(string_chunk)
        string_chunk = ""


    chunks = string_chunks

    text_and_chunks = [text_s, chunks]



    return text_and_chunks
