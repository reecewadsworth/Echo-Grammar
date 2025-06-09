from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from deepmultilingualpunctuation import PunctuationModel
import httpx

app = FastAPI()
punctuation_model = PunctuationModel()

class TextRequest(BaseModel):
    text: str

@app.post("/punctuate")
def punctuate_text(request: TextRequest):
    """Your existing punctuation endpoint—unchanged."""
    result = punctuation_model.restore_punctuation(request.text)
    return {"punctuated_text": result}

@app.post("/restore_profanities")
async def whisper_transcribe(file: UploadFile = File(...)):
    """
    New endpoint: Accepts an audio file, sends it to your Whisper Docker server,
    and returns uncensored transcription.
    """
    try:
        audio_bytes = await file.read()
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://localhost:9000/inference",  # Or your Docker host/port
                files={"file": (file.filename, audio_bytes, file.content_type)},
                data={"response_format": "json"}
            )
            response.raise_for_status()
            whisper_result = response.json()
            return {"transcript": whisper_result["text"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
