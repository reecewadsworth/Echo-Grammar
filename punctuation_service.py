from fastapi import FastAPI
from pydantic import BaseModel
from deepmultilingualpunctuation import PunctuationModel

model = PunctuationModel(model="Qishuai/distilbert_punctuator_en-base")

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/punctuate")
def punctuate_text(request: TextRequest):
    result = model.restore_punctuation(request.text)
    return {"punctuated_text": result}
