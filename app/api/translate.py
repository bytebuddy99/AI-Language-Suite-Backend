from fastapi import APIRouter

from app.schemas.translation import (
    TranslationRequest,
    TranslationResponse,
)

from app.services.translator_service import (
    translate_text,
)

from app.services.nllb_service import (
    translate_nllb,
)

router = APIRouter()


@router.post(
    "/translate",
    response_model=TranslationResponse,
)
def translate(
    request: TranslationRequest,
):

    if request.model == "nllb":

        source_lang = (
            "eng_Latn"
            if request.source_language == "en"
            else "hin_Deva"
        )

        target_lang = (
            "hin_Deva"
            if request.target_language == "hi"
            else "eng_Latn"
        )

        result = translate_nllb(
            text=request.text,
            source_lang=source_lang,
            target_lang=target_lang,
        )

    else:

        result = translate_text(
            text=request.text,
            source_language=request.source_language,
            target_language=request.target_language,
        )

    return TranslationResponse(
        original_text=request.text,
        translated_text=result,
    )