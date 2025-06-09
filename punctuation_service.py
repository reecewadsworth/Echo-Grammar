from fastapi import FastAPI, Request
from pydantic import BaseModel
from deepmultilingualpunctuation import PunctuationModel
from fastapi.responses import PlainTextResponse
from fastapi.concurrency import run_in_threadpool
from functools import lru_cache
import time

app = FastAPI()
model = PunctuationModel(model="oliverguhr/fullstop-punctuation-multilingual-sonar-base")

class TextRequest(BaseModel):
    text: str

# Loader.io verification endpoint (update the string if your code changes)
@app.get("/loaderio-8219b13a341557ee0f2794ceff9f16a2.txt")
def loaderio_verification():
    return PlainTextResponse("loaderio-8219b13a341557ee0f2794ceff9f16a2")

# LRU cache for repeated punctuation requests
@lru_cache(maxsize=1000)
def cached_punctuate(text: str):
    return model.restore_punctuation(text)

@app.post("/punctuate")
async def punctuate_text(request: TextRequest):
    # Offload CPU-bound model inference to thread pool, use cache
    result = await run_in_threadpool(cached_punctuate, request.text)
    return {"punctuated_text": result}
