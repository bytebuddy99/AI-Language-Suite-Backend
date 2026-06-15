from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Form,
)

import os

from app.services.document_service import (
    extract_text,
)

from app.services.translator_service import (
    translate_text,
)

from app.services.nllb_service import (
    translate_nllb,
)

router = APIRouter()


@router.post("/document")
async def document(
    file: UploadFile = File(...),
    model: str = Form("marian"),
    source_language: str = Form("en"),
    target_language: str = Form("hi"),
):

    upload_dir = "uploads"

    os.makedirs(
        upload_dir,
        exist_ok=True
    )

    file_path = os.path.join(
        upload_dir,
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        buffer.write(
            await file.read()
        )

    extracted_text = extract_text(
        file_path
    )

    if model == "nllb":

        translated_text = (
            translate_nllb(
                extracted_text,
                source_language,
                target_language,
            )
        )

    else:

        translated_text = (
            translate_text(
                extracted_text,
                source_language,
                target_language,
            )
        )

    return {
        "filename":
            file.filename,

        "characters":
            len(
                translated_text
            ),

        "translated_text":
            translated_text
    }   