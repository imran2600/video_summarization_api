from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import summarize1
from fastapi.staticfiles import StaticFiles
import os
app = FastAPI()

# Get the absolute path to the backend directory
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
static_dir = os.path.join(backend_dir, "backend", "static")

# Create directories if they don't exist
os.makedirs(os.path.join(static_dir, "uploads"), exist_ok=True)
os.makedirs(os.path.join(static_dir, "outputs"), exist_ok=True)

app.mount("/static", StaticFiles(directory="backend/static"), name="static")

app.include_router(summarize1.router)

# CORS (optional if front-end hosted separately)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root():
    return {"message": "Video Summarization API is running"}

