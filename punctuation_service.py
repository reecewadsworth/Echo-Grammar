from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()
punctuator = pipeline("text2text-generation", model="Qishuai/distilbert_punctuator_en")

class TextRequest(BaseModel):
    text: str

@app.post("/punctuate")
def punctuate_text(request: TextRequest):
    result = punctuator(request.text)
    return {"punctuated_text": result[0]['generated_text']}
