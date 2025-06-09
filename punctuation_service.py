from fastapi import FastAPI
from pydantic import BaseModel
from deepmultilingualpunctuation import PunctuationModel  # No auth required

app = FastAPI()
model = PunctuationModel()  # Automatically uses oliverguhr/fullstop-punctuation-multilang-large

class TextRequest(BaseModel):
    text: str

@app.post("/punctuate")
def punctuate_text(request: TextRequest):
    result = model.restore_punctuation(request.text)
    return {"punctuated_text": result}