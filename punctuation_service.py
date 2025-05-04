import os  # Add this at top
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()
# Replace the pipeline initialization with:
punctuator = pipeline("text2text-generation", model="flexudy/t5-small-multi-sentence-doctor")



class TextRequest(BaseModel):
    text: str

@app.post("/punctuate")
def punctuate_text(request: TextRequest):
    result = punctuator(request.text)
    return {"punctuated_text": result[0]['generated_text']}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))  # Use Render's PORT
    uvicorn.run(app, host="0.0.0.0", port=port)
