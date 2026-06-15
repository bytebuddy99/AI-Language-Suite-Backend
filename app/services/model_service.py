from transformers import (
    MarianMTModel,
    MarianTokenizer,
)

MODEL_PATH = (
    r"D:\AI_translator\models\marian_iitb_epoch3\marian_iitb_epoch3"
)

tokenizer = None
model = None


def load_model():

    global tokenizer
    global model

    if model is None:

        print(
            "Loading MarianMT Model..."
        )

        tokenizer = (
            MarianTokenizer
            .from_pretrained(
                MODEL_PATH
            )
        )

        model = (
            MarianMTModel
            .from_pretrained(
                MODEL_PATH
            )
        )

        print(
            "Model Loaded Successfully"
        )

    return (
        tokenizer,
        model,
    )