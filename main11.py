from tensorflow.keras.models import load_model

model = load_model("my_brain_tumor_model.keras", compile=False)
print("Model loaded successfully")


