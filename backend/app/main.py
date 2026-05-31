"""FastAPI application entry point."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routers import books, translate, images, auth, admin, lectures, paragraphs, recharge, downloads, edits, search

app = FastAPI(
    title=settings.APP_NAME,
    description="Platform for reading and translating Rudolf Steiner's works (GA series)",
    version="0.1.0",
)

# CORS — allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(books.router)
app.include_router(translate.router)
app.include_router(images.router)
app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(lectures.router)
app.include_router(paragraphs.router)
app.include_router(recharge.router)
app.include_router(downloads.router)
app.include_router(edits.router)
app.include_router(search.router)


@app.get("/")
async def root():
    return {"app": settings.APP_NAME, "status": "running"}


@app.get("/health")
async def health():
    return {"status": "ok"}
