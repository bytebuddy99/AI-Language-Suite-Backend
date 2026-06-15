from app.services.model_service import (
    load_model,
)


def translate_text(
    text: str,
    source_language: str,
    target_language: str,
):

    tokenizer, model = (
        load_model()
    )

    inputs = tokenizer(
        text,
        return_tensors="pt",
        padding=True,
    )

    generated_tokens = (
        model.generate(
            **inputs,
            max_new_tokens=128,
        )
    )

    translated_text = (
        tokenizer.decode(
            generated_tokens[0],
            skip_special_tokens=True,
        )
    )

    return translated_text