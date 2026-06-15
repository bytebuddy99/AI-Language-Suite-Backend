# AI Language Suite Backend

FastAPI backend for AI Language Suite providing text, voice, and document translation services.

## Features

* Text Translation API
* Voice Translation API
* Document Translation API
* MarianMT Integration
* NLLB Integration
* Text-to-Speech Generation
* PDF, DOCX, and TXT Processing

## Tech Stack

* FastAPI
* PyTorch
* Transformers
* MarianMT
* NLLB-200
* Uvicorn

## Installation

Create virtual environment:

```bash
python -m venv .backend_venv
```

Activate:

```bash
.backend_venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run server:

```bash
uvicorn app.main:app --reload
```

## API Endpoints

### Text Translation

```text
POST /translate
```

### Voice Translation

```text
POST /voice
```

### Document Translation

```text
POST /document
```

## Supported Languages

* English
* Hindi

## Models

* MarianMT
* NLLB-200

## Author

Rohit Sharma
