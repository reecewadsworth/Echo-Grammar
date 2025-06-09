from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel
from deepmultilingualpunctuation import PunctuationModel

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
model = PunctuationModel(model="oliverguhr/fullstop-punctuation-multilingual-sonar-base")

class TextRequest(BaseModel):
    text: str


@app.get("/loaderio-8219b13a341557ee0f2794ceff9f16a2.txt")
def loaderio_verification():
    return PlainTextResponse("loaderio-8219b13a341557ee0f2794ceff9f16a2")

@app.post("/punctuate")
def punctuate_text(request: TextRequest):
    result = model.restore_punctuation(request.text)
    return {"punctuated_text": result}
