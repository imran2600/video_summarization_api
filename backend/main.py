from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import summarize

app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI is working!"}


# CORS (optional if front-end hosted separately)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)




