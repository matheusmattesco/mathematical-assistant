from transformers import pipeline
from dotenv import load_dotenv
import os

load_dotenv()
hf_token = os.getenv("HF_TOKEN")
if not hf_token:
    raise ValueError("Hugging Face token not found in .env")
os.environ["HUGGINGFACE_HUB_TOKEN"] = hf_token

generator = pipeline(
    "text-generation",
    model="google/gemma-2b-it"
)
