from fastapi import APIRouter
from models import TextRequest
from services import generate_text
import time

router = APIRouter()

@router.post("/generate-text/")
async def generate_text_endpoint(request: TextRequest):
    start_time = time.time()
    response_text = generate_text(request.prompt)
    end_time = time.time()
    print(f"Text generation time: {end_time - start_time:.2f} seconds")
    return {"generated_text": response_text}