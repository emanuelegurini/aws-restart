from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=gemini_api_key)

config = genai.types.GenerateContentConfig(
    temperature=0.1,      # Valore tra 0.0 e 2.0
)

response = client.models.generate_content_stream(
    model="gemini-3-flash-preview", # o il modello che preferisci
    contents="Forniscimi la ricetta della carbonara sbagliata?",
    config=config
)

for chunk in response:
    # 'end=""' evita di andare a capo dopo ogni pezzetto
    # 'flush=True' forza la stampa immediata a video senza aspettare il buffer
    print(chunk.text, end="", flush=True)


