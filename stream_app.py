import streamlit as st
import requests

st.title("🧠 Brain Tumor Detection")

# Upload image
uploaded_file = st.file_uploader("Upload MRI image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    if st.button("Predict"):
        # Send file to your Modal FastAPI endpoint
        files = {"file": uploaded_file.getvalue()}
        endpoint = "https://usmansurgigram--brain-tumor-detection-serve.modal.run/predict"  

        response = requests.post(endpoint, files=files)

        if response.status_code == 200:
            result = response.json()
            st.success(f"Prediction: {result['prediction']}")
        else:
            st.error("Error connecting to the model API")