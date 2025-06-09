from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from deepmultilingualpunctuation import PunctuationModel

app = FastAPI()
app.mount("/", StaticFiles(directory="static"), name="static")  # Add this line
model = PunctuationModel(model="oliverguhr/fullstop-punctuation-multilingual-sonar-base")

class TextRequest(BaseModel):
    text: str

@app.post("/punctuate")
def punctuate_text(request: TextRequest):
    result = model.restore_punctuation(request.text)
    return {"punctuated_text": result}
