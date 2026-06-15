from fastapi import APIRouter

from app.schemas.voice import (
    VoiceRequest,
)

from app.services.voice_service import (
    text_to_speech,
)

from app.services.nllb_service import (
    translate_nllb,
)

from app.services.translator_service import (
    translate_text,
)

router = APIRouter()


@router.post("/voice")
def voice_translate(
    request: VoiceRequest,
):

    if request.model == "nllb":

        translated = translate_nllb(
            request.text,
            request.source_language,
            request.target_language,
        )

    else:

        translated = translate_text(
            request.text,
            request.source_language,
            request.target_language,
        )

    voice_file = text_to_speech(
        translated,
        request.target_language,
    )

    return {
        "recognized_text":
            request.text,

        "translated_text":
            translated,

        "audio_file":
            voice_file,
    }  