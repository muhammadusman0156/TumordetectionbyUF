import modal
from fastapi import FastAPI

app = modal.App("brain-tumor-detection")

# ✅ Define image with FastAPI + Uvicorn explicitly
my_image = modal.Image.debian_slim().pip_install(
    "fastapi", "uvicorn", "tensorflow", "numpy", "pillow"
)

# ✅ Create FastAPI app
fastapi_app = FastAPI()

@fastapi_app.get("/")
def root():
    return {"message": "FastAPI inside Modal is working 🎉"}

# ✅ Wrap FastAPI app inside Modal
@app.function(image=my_image)
@modal.asgi_app()
def serve():
    return fastapi_app