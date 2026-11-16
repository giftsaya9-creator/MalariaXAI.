import streamlit as st

# 1. Page Config
st.set_page_config(page_title="MalariaXAI Prototype", layout="wide")

# 2. Custom CSS for the Phone Mockups
st.markdown("""
<style>
    /* Hide Streamlit defaults */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Dark background */
    .stApp {
        background-color: #1e1e24;
    }
    
    /* Phone Container */
    .phone-container {
        background-color: #f4f6f9;
        border-radius: 30px;
        border: 12px solid #000000;
        padding: 20px;
        height: 650px;
        box-shadow: 0 15px 30px rgba(0,0,0,0.6);
        text-align: center;
        margin-bottom: 20px;
        position: relative;
    }
    
    /* Top App Header */
    .app-header {
        background-color: #2b5797;
        color: white;
        padding: 12px;
        border-radius: 8px;
        font-weight: bold;
        font-size: 18px;
        margin-bottom: 25px;
        font-family: sans-serif;
    }
    
    /* Buttons */
    .phone-btn {
        background-color: white;
        border: 1px solid #ccc;
        padding: 14px;
        margin: 10px 0;
        border-radius: 8px;
        font-size: 15px;
        color: #333;
        width: 100%;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .scan-btn {
        background-color: #27ae60;
        color: white;
        border: none;
    }
    .save-btn {
        background-color: #27ae60;
        color: white;
        border: none;
        width: 45%;
        display: inline-block;
    }
    .flag-btn {
        background-color: white;
        color: #c0392b;
        border: 1px solid #c0392b;
        width: 45%;
        display: inline-block;
        margin-left: 5%;
    }
    
    /* Text Styles */
    .red-text { color: #c0392b; font-weight: 900; font-size: 22px; margin-top: 15px; letter-spacing: 1px;}
    .small-text { color: #7f8c8d; font-size: 13px; }
    
    /* Camera Box */
    .camera-box {
        border: 2px dashed #bdc3c7;
        background-color: #ecf0f1;
        height: 250px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #95a5a6;
        margin: 25px 0;
        border-radius: 10px;
    }
    
    /* History Rows */
    .history-row {
        display: flex;
        justify-content: space-between;
        padding: 15px;
        border-bottom: 1px solid #e0e0e0;
        font-size: 14px;
        color: #333;
    }
    .highlight-row {
        background-color: #fcf3cf;
    }
</style>
""", unsafe_allow_html=True)

# Main Title
st.markdown("<h2 style='text-align: center; color: white; margin-bottom: 40px;'>Mobile App Interface Prototype</h2>", unsafe_allow_html=True)

# Create 3 columns for the screens
col1, col2, col3 = st.columns(3)

# --- SCREEN 1: HOME ---
with col1:
    st.markdown("""<div class="phone-container"><div class="app-header">MalariaXAI</div><div class="camera-box">[ camera view ]</div><div class="phone-btn scan-btn">Scan smear</div><div class="phone-btn">Choose from gallery</div><div class="phone-btn">History</div><p class="small-text" style="color:#c0392b; margin-top: 30px;">Decision-support tool only</p><p class="small-text" style="position: absolute; bottom: 10px; left: 0; width: 100%;">(a) Home / capture</p></div>""", unsafe_allow_html=True)

# --- SCREEN 2: RESULT ---
with col2:
    st.markdown("""<div class="phone-container"><div class="app-header">Result</div><div style="width: 180px; height: 180px; background: radial-gradient(circle, red, blue, yellow); border-radius: 50%; margin: 0 auto; box-shadow: 0 4px 8px rgba(0,0,0,0.3);"></div><div class="red-text">PARASITISED</div><p class="small-text" style="margin-top: 10px;">Confidence: 0.96 (example)</p><p class="small-text">Time on phone: 0.4 s (example)</p><p class="small-text" style="color: #c0392b; margin-top: 10px;">Red = region that drove the decision</p><div style="margin-top: 40px;"><div class="phone-btn save-btn">Save</div><div class="phone-btn flag-btn">Flag wrong</div></div><p class="small-text" style="position: absolute; bottom: 10px; left: 0; width: 100%;">(b) Result with Grad-CAM</p></div>""", unsafe_allow_html=True)

# --- SCREEN 3: HISTORY ---
with col3:
    st.markdown("""<div class="phone-container"><div class="app-header">History</div><div class="history-row"><span>001</span><span>Parasitised</span><span>0.97</span></div><div class="history-row"><span>002</span><span>Uninfected</span><span>0.99</span></div><div class="history-row highlight-row"><span>003</span><span>Uninfected</span><span>0.62</span></div><div class="history-row"><span>004</span><span>Parasitised</span><span>0.91</span></div><div class="history-row"><span>005</span><span>Uninfected</span><span>0.95</span></div><p class="small-text" style="text-align: left; margin-top: 30px; font-style: italic; color: #95a5a6; padding: 0 15px;">Highlighted row = flagged or low-confidence case for review</p><p class="small-text" style="position: absolute; bottom: 10px; left: 0; width: 100%;">(c) History and review</p></div>""", unsafe_allow_html=True)
