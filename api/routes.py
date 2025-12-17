from fastapi import APIRouter
from pydantic import BaseModel

from core.pipeline import normalize_text

router = APIRouter()

class FormatRequest(BaseModel):
    text: str

class FormatResponse(BaseModel):
    formatted_text: str


@router.post("/format", response_model=FormatResponse)
def format_text(payload: FormatRequest):
    return FormatResponse(
        formatted_text=normalize_text(payload.text)
    )

@router.get("/health")
def health():
    return {"status": "ok"}
