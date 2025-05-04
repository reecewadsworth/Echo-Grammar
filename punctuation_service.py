from fastapi import FastAPI
from pydantic import BaseModel
from deepmultilingualpunctuation import PunctuationModel  # Changed import

app = FastAPI()
model = PunctuationModel()  # Use the working model

class TextRequest(BaseModel):
    text: str

@app.post("/punctuate")
def punctuate_text(request: TextRequest):
    result = model.restore_punctuation(request.text)
    return {"punctuated_text": result}
