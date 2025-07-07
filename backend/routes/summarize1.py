from fastapi import APIRouter, UploadFile, File  # Add these imports if missing
from backend.utils.file_utils import save_uploaded_file
from backend.services.extractor import extract_features
from backend.services.model_loader import load_model
from backend.services.summarizer2 import get_scores, get_selected_indices, save_summary_video
from backend.config import UPLOAD_DIR, OUTPUT_DIR
import os

router = APIRouter()

# @router.post("/summarize")
# async def summarize_video(video: UploadFile = File(...)):  # <-- Add this decorator
#     # Save uploaded file
#     video_path = os.path.join(UPLOAD_DIR, video.filename)
#     with open(video_path, "wb") as f:
#         f.write(await video.read())
#     features, picks = extract_features(video_path)
#     model = load_model()
#     scores = get_scores(model, features)
#     selected = get_selected_indices(scores, picks)
#     output_path = f"{OUTPUT_DIR}/summary_{video.filename}"
#     save_summary_video(video_path, selected, output_path)
#     return {"summary_video_path": f"/static/outputs/summary_{video.filename}"}

@router.post("/summarize")
async def summarize_video(video: UploadFile = File(...)):
    try:
        # Save uploaded file
        video_path = save_uploaded_file(video, UPLOAD_DIR)
        
        # Load model (now with proper path handling)
        model = load_model()  # Uses default path
        
        # Rest of your processing...
        features, picks = extract_features(video_path)
        scores = get_scores(model, features)
        selected = get_selected_indices(scores, picks)
        
        output_path = f"{OUTPUT_DIR}/summary_{video.filename}"
        save_summary_video(video_path, selected, output_path)
        
        return {"summary_video_path": f"/static/outputs/summary_{video.filename}"}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

from backend.services.model_loader import load_model
model = load_model()  # Should work
print(model.device)