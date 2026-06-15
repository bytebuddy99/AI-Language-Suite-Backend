from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
)

MODEL_PATH = r"D:\AI_LANGUAGE_SUITE\final_nllb_200k"

tokenizer = None
model = None


def load_nllb():

    global tokenizer
    global model

    if tokenizer is None or model is None:

        print(
            "Loading NLLB Model..."
        )

        tokenizer = (
            AutoTokenizer.from_pretrained(
                MODEL_PATH,
                local_files_only=True,
            )
        )

        model = (
            AutoModelForSeq2SeqLM.from_pretrained(
                MODEL_PATH,
                local_files_only=True,
            )
        )

        print(
            "NLLB Loaded Successfully!"
        )

    return tokenizer, model


def translate_nllb(
    text: str,
    source_lang: str,
    target_lang: str,
):

    LANGUAGE_MAP = {
        "en": "eng_Latn",
        "hi": "hin_Deva",
    }

    source_lang = LANGUAGE_MAP.get(
        source_lang,
        source_lang,
    )

    target_lang = LANGUAGE_MAP.get(
        target_lang,
        target_lang,
    )

    tokenizer, model = load_nllb()

    tokenizer.src_lang = source_lang

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=512,
    )

    outputs = model.generate(
        **inputs,
        forced_bos_token_id=
        tokenizer.convert_tokens_to_ids(
            target_lang
        ),
        max_length=256,
        num_beams=4,
    )

    translated_text = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True,
    )

    return translated_text