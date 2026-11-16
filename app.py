import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import time 

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="MalariaXAI Diagnostic", page_icon="🦟", layout="wide")

# --- CUSTOM CSS FOR BEAUTIFICATION ---
st.markdown("""
    <style>
    .stApp { background-color: #f8fafc; }
    h1 { color: #0f172a; font-family: 'Helvetica Neue', sans-serif; font-weight: 800; }
    .subtitle { color: #64748b; font-size: 16px; margin-bottom: 30px; }
    .result-card { padding: 20px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    .parasitized { background-color: #fef2f2; border-left: 6px solid #ef4444; }
    .uninfected { background-color: #f0fdf4; border-left: 6px solid #22c55e; }
    .metric-title { font-size: 14px; color: #64748b; font-weight: 600; margin-bottom: 5px; }
    .metric-value { font-size: 24px; font-weight: 800; color: #1e293b; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1>🦟 MalariaXAI Diagnostic Center</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'><b>Explainable AI-Based Malaria Parasite Detection System</b> | Gift Saya (202302133)</p>", unsafe_allow_html=True)
st.divider()

# --- LOAD MODEL ---
@st.cache_resource
def load_model():
    try:
        # Load the model you uploaded to GitHub
        model = tf.keras.models.load_model('malaria_model.keras')
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}. Please ensure 'malaria_model.keras' is in the repository.")
        return None

model = load_model()

# --- GRAD-CAM FUNCTION ---
def make_gradcam_heatmap(img_array, model, last_conv_layer_name):
    # Create a model that maps the input image to the activations of the last conv layer
    grad_model = tf.keras.models.Model(
        [model.inputs], [model.get_layer(last_conv_layer_name).output, model.output]
    )

    with tf.GradientTape() as tape:
        last_conv_layer_output, preds = grad_model(img_array)
        class_channel = preds[:, 0]

    grads = tape.gradient(class_channel, last_conv_layer_output)
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))
    last_conv_layer_output = last_conv_layer_output[0]
    heatmap = last_conv_layer_output @ pooled_grads[..., tf.newaxis]
    heatmap = tf.squeeze(heatmap)
    heatmap = tf.maximum(heatmap, 0) / tf.math.reduce_max(heatmap)
    return heatmap.numpy()

# --- MAIN LAYOUT ---
col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    st.subheader("📸 1. Upload Sample")
    uploaded_file = st.file_uploader("Upload a microscopic blood smear image", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, caption='Uploaded Image', use_container_width=True)

with col2:
    st.subheader("🔬 2. AI Analysis & Explanation")
    
    if uploaded_file is not None and model is not None:
        with st.spinner('Analyzing image with MobileNetV2...'):
            time.sleep(0.5) # Small delay for UX
            
            # Preprocess
            img = image.resize((224, 224))
            img_array = np.array(img) / 255.0
            img_array_expanded = np.expand_dims(img_array, axis=0)
            
            # Predict
            prediction_prob = model.predict(img_array_expanded)[0][0]
            
            # Determine result
            if prediction_prob > 0.5:
                label = "PARASITIZED"
                confidence = prediction_prob * 100
                card_class = "parasitized"
            else:
                label = "UNINFECTED"
                confidence = (1 - prediction_prob) * 100
                card_class = "uninfected"

        # --- DISPLAY RESULT CARD ---
        st.markdown(f"""
            <div class="result-card {card_class}">
                <div class="metric-title">Diagnosis</div>
                <div class="metric-value" style="color: {'#ef4444' if label == 'PARASITIZED' else '#22c55e'};">{label}</div>
                <br>
                <div style="display: flex; gap: 40px;">
                    <div>
                        <div class="metric-title">Confidence</div>
                        <div class="metric-value">{confidence:.1f}%</div>
                    </div>
                    <div>
                        <div class="metric-title">Inference Time</div>
                        <div class="metric-value">~0.4s</div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # --- GENERATE GRAD-CAM ---
        st.write("### 🧠 AI Explanation (Grad-CAM)")
        st.write("The heatmap below shows where the AI focused to make its decision (Red = High Focus).")
        
        try:
            # Find the last conv layer of MobileNetV2
            base_model = model.layers[0]
            last_conv_layer_name = base_model.layers[-3].name 
            
            # Generate heatmap
            heatmap = make_gradcam_heatmap(img_array_expanded, base_model, last_conv_layer_name)
            
            # Overlay heatmap on original image
            img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            heatmap_resized = cv2.resize(heatmap, (img_cv.shape[1], img_cv.shape[0]))
            heatmap_colored = cv2.applyColorMap(np.uint8(255 * heatmap_resized), cv2.COLORMAP_JET)
            superimposed = cv2.addWeighted(img_cv, 0.6, heatmap_colored, 0.4, 0)
            superimposed = cv2.cvtColor(superimposed, cv2.COLOR_BGR2RGB)
            
            st.image(superimposed, caption="Grad-CAM: Red regions drove the prediction", use_container_width=True)
            
        except Exception as e:
            st.warning("Could not generate heatmap. Ensure the model layer names match.")
        
        st.info("💡 **Clinical Note:** This tool is a decision-support system. Always confirm with a laboratory professional.")
    
    elif model is None:
        st.warning("Waiting for model to load...")
    else:
        st.info("👈 Please upload an image on the left to begin analysis.")

# --- FOOTER ---
st.divider()
st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>Mulungushi University | School of Engineering and Technology | 2026</p>", unsafe_allow_html=True)
