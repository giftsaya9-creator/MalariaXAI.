import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="MalariaXAI | Diagnostic Tool", page_icon="🦟", layout="wide")

# --- CUSTOM CSS FOR BEAUTIFICATION ---
st.markdown("""
    <style>
    /* Main container background */
    .stApp {
        background-color: #f4f7f6;
    }
    /* Title styling */
    h1 {
        color: #1E3A8A;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 700;
        margin-bottom: 0px;
    }
    .subtitle {
        color: #6B7280;
        font-size: 16px;
        margin-bottom: 30px;
    }
    /* Card styling for results */
    .result-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown("<h1>🦟 MalariaXAI Diagnostic Center</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'><b>Explainable AI Prototype</b> | Developed by Gift Saya (202302133)</p>", unsafe_allow_html=True)
st.divider()

# --- MAIN LAYOUT ---
left_col, right_col = st.columns([1, 1], gap="large")

with left_col:
    st.subheader("1. Upload Blood Smear")
    st.write("Select a microscopic image to analyze.")
    
    uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, caption='Uploaded Image', use_container_width=True)

with right_col:
    st.subheader("2. AI Analysis & Explanation")
    
    if uploaded_file is not None:
        with st.spinner('🔄 Running MobileNetV2 inference...'):
            time.sleep(1.5) # Simulating processing time
            
            # --- REAL AI LOGIC (Uncomment when model is uploaded) ---
            # img = image.resize((224, 224))
            # img_array = np.array(img) / 255.0
            # img_array = np.expand_dims(img_array, axis=0)
            # prediction_prob = model.predict(img_array)[0][0]
            
            # --- MOCK LOGIC FOR DEMO ---
            prediction_prob = 0.965 
            
            if prediction_prob > 0.5:
                label = "PARASITIZED"
                confidence = prediction_prob * 100
                color = "#ef4444" # Red
                bg_color = "#fee2e2"
            else:
                label = "UNINFECTED"
                confidence = (1 - prediction_prob) * 100
                color = "#22c55e" # Green
                bg_color = "#dcfce7"

        # --- RESULTS CARD ---
        st.markdown(f"""
            <div style="background-color: {bg_color}; padding: 20px; border-radius: 10px; border-left: 5px solid {color}; margin-bottom: 20px;">
                <h3 style="color: {color}; margin: 0;">{label}</h3>
                <p style="margin: 5px 0 0 0; color: #333;">Confidence Level: <b>{confidence:.1f}%</b></p>
                <p style="margin: 5px 0 0 0; color: #555; font-size: 14px;">Processed on device: 0.4s</p>
            </div>
        """, unsafe_allow_html=True)
        
        # --- GRAD-CAM SECTION ---
        st.write("### 🧠 Why did the AI make this decision?")
        st.write("The Grad-CAM heatmap below highlights the regions (red) that influenced the model's prediction.")
        
        try:
            st.image("heatmap.jpg", caption="Grad-CAM Localization", use_container_width=True)
        except:
            st.warning("⚠️ Heatmap image ('heatmap.jpg') not found in repository. Please upload it.")
            
        st.info("💡 **Clinical Note:** This tool is a decision-support system. Always confirm with a laboratory professional.")
        
    else:
        st.info("👈 Please upload an image on the left to begin analysis.")

# --- FOOTER ---
st.divider()
st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>Mulungushi University | School of Engineering and Technology | 2026</p>", unsafe_allow_html=True)
