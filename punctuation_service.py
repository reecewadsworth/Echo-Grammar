from fastapi import FastAPI
from pydantic import BaseModel
from deepmultilingualpunctuation import PunctuationModel
from fastapi.responses import PlainTextResponse

app = FastAPI()
model = PunctuationModel()

# Loader.io verification endpoint (no static mounting needed)
@app.get("/loaderio-8219b13a341557ee0f2794ceff9f16a2.txt")
def loaderio_verification():
    return PlainTextResponse("loaderio-8219b13a341557ee0f2794ceff9f16a2")

class TextRequest(BaseModel):
    text: str

@app.post("/punctuate")
def punctuate_text(request: TextRequest):
    result = model.restore_punctuation(request.text)
    return {"punctuated_text": result}
