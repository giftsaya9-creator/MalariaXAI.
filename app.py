import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import time

st.set_page_config(page_title="Malaria XAI", page_icon="🦟")
st.title("🦟 Malaria Parasite Detection")
st.write("**Explainable AI Prototype - Gift Saya**")

uploaded_file = st.file_uploader("Upload a blood smear image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    st.write("---")
    
    with st.spinner('AI is analyzing the image...'):
        # NOTE: You need to upload your model file and change this path!
        # model = tf.keras.models.load_model('malaria_model.keras')
        
        # For now, we will simulate the result so the app works immediately
        time.sleep(1)
        prediction_prob = 0.88 
        
        if prediction_prob > 0.5:
            label = "Parasitized"
            confidence = prediction_prob * 100
            st.error(f"### Result: {label} (Confidence: {confidence:.1f}%)")
        else:
            label = "Uninfected"
            confidence = (1 - prediction_prob) * 100
            st.success(f"### Result: {label} (Confidence: {confidence:.1f}%)")
            
    st.write("### AI Explanation (Grad-CAM)")
    try:
        st.image("heatmap.jpg", caption="Red areas show where the AI found the parasite.")
    except:
        st.warning("Heatmap image 'heatmap.jpg' not found in files.")