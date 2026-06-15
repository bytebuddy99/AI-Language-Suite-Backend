from pydantic import (
    BaseModel,
)


class TranslationRequest(
    BaseModel
):
    text: str
    source_language: str
    target_language: str
    model: str = "marian"


class TranslationResponse(
    BaseModel
):
    original_text: str
    translated_text: str