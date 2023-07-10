from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import re
from deep_translator import GoogleTranslator
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the request payload schema
class TranslationRequest(BaseModel):
    text: str
    source: Optional[str] = None
    target: str

# Split the text into smaller groups up to 5000 characters without breaking lines so need to split on new lines
def split_text(text, max_len=4500):
    # Split the text into lines
    lines = text.split("\n")
    # List of chunks
    chunks = []
    # Chunk buffer
    chunk = ""

    # Loop through the lines
    for line in lines:
        # If the chunk is too long, add it to the list and reset the chunk
        if len(chunk + line) > max_len:
            chunks.append(chunk)
            chunk = ""
        # Add the line to the chunk
        chunk += line + "\n"

    # Add the last chunk to the list
    if chunk:
        chunks.append(chunk)

    # Return the list of chunks
    return chunks

@app.post("/translate")
def translate_text(request: TranslationRequest):
    # Get the input values from the request payload
    text = request.text
    source = request.source
    target = request.target

    # Translate the main text
    chunks = split_text(text)
    translated_text = ''
    for chunk in chunks:
        if source is None:
            source = 'auto'
        translated = GoogleTranslator(source=source, target=target).translate(text=chunk)
        translated_text += translated + "\n"
        
    # Remove extra new lines
    translated_text = re.sub(r'[\n]{3,}', '\n\n', translated_text.strip())
    translated_text = translated_text.strip()

    # Return the translated text
    return { 'text': translated_text }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
