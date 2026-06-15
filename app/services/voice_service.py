from gtts import gTTS
import uuid
import os

VOICE_DIR = "generated_audio"

os.makedirs(
    VOICE_DIR,
    exist_ok=True,
)


def text_to_speech(
    text: str,
    language: str,
):

    language_map = {
        "hi": "hi",
        "en": "en",
        "hin_Deva": "hi",
        "eng_Latn": "en",
    }

    tts_language = (
        language_map.get(
            language,
            "en"
        )
    )

    filename = (
        f"{uuid.uuid4()}.mp3"
    )

    path = os.path.join(
        VOICE_DIR,
        filename,
    )

    tts = gTTS(
        text=text,
        lang=tts_language,
    )

    tts.save(path)

    return path