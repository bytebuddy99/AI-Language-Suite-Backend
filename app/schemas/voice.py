from pydantic import BaseModel


class VoiceRequest(
    BaseModel
):
    text: str
    source_language: str
    target_language: str
    model: str