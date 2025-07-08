from fastapi import APIRouter, UploadFile, HTTPException, File  # Add these imports if missing
from backend.utils.file_utils import save_uploaded_file
from backend.services.extractor import extract_features
from backend.services.model_loader import load_model
from backend.services.summarizer2 import get_scores, get_selected_indices, save_summary_video
from backend.config import UPLOAD_DIR, OUTPUT_DIR
import os

router = APIRouter()
from fastapi.responses import JSONResponse
import os

router = APIRouter()

# @router.post("/summarize")
# async def summarize_video(video: UploadFile = File(..., media_type="video/mp4")):
#     try:
#         # Validate file type
#         if not video.filename.lower().endswith(('.mp4', '.mov', '.avi')):
#             raise HTTPException(
#                 status_code=415,
#                 detail="Only MP4, MOV, or AVI files are supported"
#             )

#         # Save uploaded file
#         video_path = save_uploaded_file(video, UPLOAD_DIR)
        
#         # Process video
#         model = load_model()
#         features, picks = extract_features(video_path)
#         scores = get_scores(model, features)
#         selected = get_selected_indices(scores, picks)
        
#         # Generate output
#         output_filename = f"summary_{os.path.basename(video.filename)}"
#         output_path = os.path.join(OUTPUT_DIR, output_filename)
#         save_summary_video(video_path, selected, output_path)
        
#         return JSONResponse({
#             "status": "success",
#             "summary_path": f"/static/outputs/{output_filename}"
#         })
        
#     except HTTPException:
#         raise
#     except Exception as e:
#         raise HTTPException(
#             status_code=500,
#             detail=f"Processing failed: {str(e)}"
#         )





# @router.post("/summarize", response_model=dict)
# async def summarize_video(video: UploadFile = File(...)):
#     try:
#         # [Your existing processing code...]
        
#         return {
#             "status": "success",
#             "summary_video_path": f"/static/outputs/summary_{video.filename}",
#             "message": "Video processed successfully"
#         }
        
#     except Exception as e:
#         raise HTTPException(
#             status_code=500,
#             detail={
#                 "status": "error",
#                 "message": str(e)
#             }
#         )






@router.post("/summarize", response_model=dict)
async def summarize_video(video: UploadFile = File(...)):
    try:
        # 1. Validate file
        if not video.filename.lower().endswith(('.mp4', '.mov', '.avi')):
            raise HTTPException(status_code=400, detail="Invalid file format")

        # 2. Process video (your existing code)
        video_path = save_uploaded_file(video, UPLOAD_DIR)
        model = load_model()
        features, picks = extract_features(video_path)
        scores = get_scores(model, features)
        selected = get_selected_indices(scores, picks)
        
        # 3. Generate output
        output_filename = f"summary_{video.filename}"
        output_path = f"{OUTPUT_DIR}/{output_filename}"
        save_summary_video(video_path, selected, output_path)

        # 4. Return consistent response
        return {
            "status": "success",
            "output_path": f"/static/outputs/{output_filename}",
            "download_url": f"http://localhost:8000/static/outputs/{output_filename}"
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "status": "error",
                "message": str(e)
            }
        )