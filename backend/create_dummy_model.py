# backend/create_dummy_model.py
import torch
from layers.summarizer3 import PGL_SUM

# Initialize model with correct architecture
dummy_model = PGL_SUM(
    input_size=1024,
    output_size=1024,
    num_segments=4,
    heads=8,
    fusion="add",
    pos_enc="absolute"
)

# Save to the correct location
torch.save(dummy_model.state_dict(), "Model/epoch-199.pkl")
print("✅ Dummy model created at Model/epoch-199.pkl")