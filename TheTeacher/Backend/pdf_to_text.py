
from PyPDF2 import PdfReader
from pprint import pprint

# maybe remove header, footer and shi

pdf = r"C:\Users\pokhr\OneDrive\Desktop\Current_elecf.pdf"


def text_extractor(filepath):

    reader = PdfReader(filepath)
    text = ""

    pages = reader.pages

    for page in pages :
        page_text = page.extract_text()
        text += page_text

    return text

#pprint(len(text_extractor(pdf).split()))