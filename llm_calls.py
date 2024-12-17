import google.generativeai as genai
from dotenv import load_dotenv
import os
import typing_extensions as typing

class Flashcard(typing.TypedDict):
    front: str
    back: str
flashcard_prompt = "Create flashcards for the core concepts in the paper. If needed, use MathJAX and enclose in $ for mathematical typesetting. Prioritize the novel concepts from the paper, like new architecture, experiments, or results. Try to make 2 to 3 cards for each page of the paper before the references. Think it through before making the flashcards. "

def getPrompt(count:int, prompt:int = 0):
    return f"Create flashcards for the core concepts in the paper. If needed, use MathJAX and enclose in $ for mathematical typesetting. Prioritize the novel concepts from the paper, like new architecture, experiments, or results. Make {count} distinct cards. Think it through before making the flashcards. "
def callGemini():
    load_dotenv()

    gemini_api_key = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key = gemini_api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content("Who is the current president?")
    print(response.text)

def readPDF(pdf_path: str, count: int, prompt: int = 0):
    load_dotenv()
    gemini_api_key = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key = gemini_api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    uploaded_pdf = genai.upload_file(path=pdf_path)
    response = model.generate_content([uploaded_pdf, getPrompt(count = count)],
                                      generation_config = genai.GenerationConfig(
                                          response_mime_type="application/json", response_schema = list[Flashcard]))
    return response

