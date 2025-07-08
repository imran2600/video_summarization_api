from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import summarize1
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Improved static files configuration
static_dir = os.path.join(os.path.dirname(__file__), "static")
os.makedirs(os.path.join(static_dir, "uploads"), exist_ok=True)
os.makedirs(os.path.join(static_dir, "outputs"), exist_ok=True)

app.mount("/static", StaticFiles(directory=static_dir), name="static")
@app.get("/generate-summary")
async def generate_summary():
    return {
        "status": "success",
        "download_url": "http://localhost:8000/static/outputs/summary_l1.mp4",
        "filename": "summary_l1.mp4"
    }
app.include_router(summarize1.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

