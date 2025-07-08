# import torch
# import os
# from pathlib import Path
# from layers.summarizer3 import PGL_SUM
# from backend.config import DEVICE

# def load_model(weights_path):
#     try:
#         # 1. Convert to absolute path
#         base_dir = Path(__file__).parent.parent  # backend/ directory
#         model_path = (base_dir / weights_path).resolve()  # Full absolute path
        
#         # 2. Verify file exists
#         if not model_path.exists():
#             available_files = "\n".join(f"- {f}" for f in base_dir.glob("**/*.pkl"))
#             raise FileNotFoundError(
#                 f"Model file not found at: {model_path}\n"
#                 f"Available .pkl files:\n{available_files or 'None found'}"
#             )

#         # 3. Initialize model with proper device handling
#         model = PGL_SUM(
#             input_size=1024,
#             output_size=1024,
#             num_segments=4,
#             heads=8,
#             fusion="add",
            
#         )  # Move model to device immediately

#         # 4. Verify file is not empty
#         if os.path.getsize(model_path) == 0:
#             raise ValueError(f"Model file is empty (0 bytes): {model_path}")

#         # 5. Load weights with device mapping
#         state_dict = torch.load(model_path, map_location=DEVICE)
        
#         # 6. Handle potential state_dict issues
#         if not isinstance(state_dict, dict):
#             raise ValueError("Loaded state_dict is not a dictionary")
            
#         # 7. Load state dict with strict=False for compatibility
#         model.load_state_dict(state_dict, strict=False)
#         model.eval()
        
#         # 8. Verify model is on correct device
#         if next(model.parameters()).device != torch.device(DEVICE):
#             raise RuntimeError(f"Model not on expected device {DEVICE}")
        
#         print(f"✅ Successfully loaded model from: {model_path}")
#         print(f"Model device: {next(model.parameters()).device}")
#         return model
        
#     except Exception as e:
#         # Detailed error reporting
#         error_msg = (
#             f"🚨 Model loading failed\n"
#             f"Attempted path: {weights_path}\n"
#             f"Absolute path: {model_path if 'model_path' in locals() else 'N/A'}\n"
#             f"Base directory: {base_dir}\n"
#             f"Current device: {DEVICE}\n"
#             f"CUDA available: {torch.cuda.is_available()}\n"
#             f"Error type: {type(e).__name__}\n"
#             f"Details: {str(e)}"
#         )
#         raise RuntimeError(error_msg) from e
import torch
from pathlib import Path
from layers.summarizer3 import PGL_SUM
from backend.config import DEVICE

def load_model(weights_path=r"D:\video_summarization_api-main\video_summarization_api-main\backend\Model\epoch-199.pkl"):
    """
    Load PGL-SUM model with weights
    Args:
        weights_path: Path to model weights (defaults to project location)
    """
    try:
        # Convert to absolute path
        model_path = Path(weights_path).absolute()
        
        # Verify file exists
        if not model_path.exists():
            raise FileNotFoundError(f"Model weights not found at: {model_path}")

        # Initialize model
        model = PGL_SUM(
            input_size=1024,
            output_size=1024,
            num_segments=4,
            heads=8,
            fusion="add"
        ).to(DEVICE)

        # Load weights
        state_dict = torch.load(model_path, map_location=DEVICE)
        model.load_state_dict(state_dict)
        model.eval()
        
        return model

    except Exception as e:
        raise RuntimeError(f"Model loading failed: {str(e)}")