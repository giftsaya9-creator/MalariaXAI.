import streamlit as st
import time

# 1. Page Config
st.set_page_config(page_title="MalariaXAI Prototype", layout="wide")

# 2. Custom CSS to make it look like Phone Mockups
st.markdown("""
<style>
    /* Hide the Streamlit header and menu */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Dark background for the whole page */
    .stApp {
        background-color: #2b2b2b;
    }
    
    /* Phone Container Styling */
    .phone-container {
        background-color: white;
        border-radius: 30px;
        border: 12px solid #1a1a1a;
        padding: 20px;
        min-height: 600px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.5);
        text-align: center;
        margin-bottom: 20px;
    }
    
    /* Top Bar of the App */
    .app-header {
        background-color: #2b5797;
        color: white;
        padding: 10px;
        border-radius: 5px;
        font-weight: bold;
        margin-bottom: 20px;
        font-family: sans-serif;
    }
    
    /* Buttons inside the phone */
    .phone-btn {
        background-color: white;
        border: 1px solid #ccc;
        padding: 12px;
        margin: 8px 0;
        border-radius: 5px;
        cursor: pointer;
        font-size: 14px;
        color: #333;
        width: 100%;
    }
    .scan-btn {
        background-color: #4CAF50;
        color: white;
        border: none;
    }
    .save-btn {
        background-color: #4CAF50;
        color: white;
        border: none;
        width: 45%;
        display: inline-block;
    }
    .flag-btn {
        background-color: white;
        color: #d9534f;
        border: 1px solid #d9534f;
        width: 45%;
        display: inline-block;
        margin-left: 5%;
    }
    
    /* Text colors */
    .red-text { color: #d9534f; font-weight: bold; font-size: 20px; margin-top: 15px;}
    .small-text { color: gray; font-size: 12px; }
    
    /* Camera placeholder */
    .camera-box {
        border: 2px dashed #999;
        height: 250px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #999;
        margin: 20px 0;
    }
    
    /* History rows */
    .history-row {
        display: flex;
        justify-content: space-between;
        padding: 12px;
        border-bottom: 1px solid #eee;
        font-size: 14px;
        color: #333;
    }
    .highlight-row {
        background-color: #fff3cd;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: white;'>Figure 2.2: Mock-up of the home, result and history screens</h2>", unsafe_allow_html=True)

# Create 3 columns for the 3 screens
col1, col2, col3 = st.columns(3)

# --- SCREEN 1: HOME ---
with col1:
    st.markdown("""
    <div class="phone-container">
        <div class="app-header">MalariaXAI</div>
        <div class="camera-box">[ camera view ]</div>
        <div class="phone-btn scan-btn">Scan smear</div>
        <div class="phone-btn">Choose from gallery</div>
        <div class="phone-btn">History</div>
        <p class="small-text" style="color:#d9534f; margin-top: 30px;">Decision-support tool only</p>
        <p class="small-text" style="margin-top: 40px;">(a) Home / capture</p>
    </div>
    """, unsafe_allow_html=True)

# --- SCREEN 2: RESULT ---
with col2:
    st.markdown("""
    <div class="phone-container">
        <div class="app-header">Result</div>
        <img src="https://raw.githubusercontent.com/tensorflow/examples/master/lite/examples/image_classification/android/app/src/main/res/drawable/ic_launcher_background.png" style="width: 200px; height: 200px; border-radius: 50%; object-fit: cover; margin-bottom: 10px;" />
        <!-- Note: The image above is a placeholder. If you want your actual heatmap, you need to use st.image() below instead of raw HTML -->
        
        <div class="red-text">PARASITISED</div>
        <p class="small-text">Confidence: 0.96 (example)</p>
        <p class="small-text">Time on phone: 0.4 s (example)</p>
        <p class="small-text" style="color: #d9534f;">Red = region that drove the decision</p>
        
        <div style="margin-top: 30px;">
            <div class="phone-btn save-btn">Save</div>
            <div class="phone-btn flag-btn">Flag wrong</div>
        </div>
        <p class="small-text" style="margin-top: 40px;">(b) Result with Grad-CAM</p>
    </div>
    """, unsafe_allow_html=True)

# --- SCREEN 3: HISTORY ---
with col3:
    st.markdown("""
    <div class="phone-container">
        <div class="app-header">History</div>
        <div class="history-row"><span>001</span><span>Parasitised</span><span>0.97</span></div>
        <div class="history-row"><span>002</span><span>Uninfected</span><span>0.99</span></div>
        <div class="history-row highlight-row"><span>003</span><span>Uninfected</span><span>0.62</span></div>
        <div class="history-row"><span>004</span><span>Parasitised</span><span>0.91</span></div>
        <div class="history-row"><span>005</span><span>Uninfected</span><span>0.95</span></div>
        
        <p class="small-text" style="text-align: left; margin-top: 40px; font-style: italic; color: #a0a0a0;">
            Highlighted row = flagged or low-confidence case for review
        </p>
        <p class="small-text" style="margin-top: 20px;">(c) History and review</p>
    </div>
    """, unsafe_allow_html=True)
