from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.api.translate import (
    router as translate_router,
)

from app.api.voice import (
    router as voice_router,
)
from app.api.document import (
    router as document_router,
)


app = FastAPI(
    title="AI Language Suite API",
    version="1.0.0",
)

app.mount(
    "/generated_audio",
    StaticFiles(
        directory="generated_audio"
    ),
    name="generated_audio",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    translate_router
)

app.include_router(
    voice_router
)
app.include_router(
    document_router
)


@app.get("/")
def root():
    return {
        "status": "running",
        "message": "AI Language Suite API",
    }