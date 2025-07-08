

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import torch

# config.py
import torch
UPLOAD_DIR = "backend/static/uploads"
OUTPUT_DIR = "backend/static/outputs"
FRAME_RATE = 15
SCORE_THRESHOLD = 0.4
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="backend/static"), name="static")
