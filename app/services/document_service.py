import fitz
from docx import Document
import os


def extract_pdf_text(
    file_path: str,
):

    text = ""

    pdf = fitz.open(
        file_path
    )

    for page in pdf:

        text += (
            page.get_text()
            + "\n"
        )

    pdf.close()

    return text


def extract_docx_text(
    file_path: str,
):

    doc = Document(
        file_path
    )

    text = "\n".join(
        [
            paragraph.text
            for paragraph in doc.paragraphs
        ]
    )

    return text


def extract_txt_text(
    file_path: str,
):

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()


def extract_text(
    file_path: str,
):

    extension = (
        os.path.splitext(
            file_path
        )[1]
        .lower()
    )

    if extension == ".pdf":

        return extract_pdf_text(
            file_path
        )

    if extension == ".docx":

        return extract_docx_text(
            file_path
        )

    if extension == ".txt":

        return extract_txt_text(
            file_path
        )

    raise ValueError(
        f"Unsupported file type: {extension}"
    )