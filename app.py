import streamlit as st

st.set_page_config(page_title="MalariaXAI Prototype", layout="centered")

# Custom CSS for styling
st.markdown("""
<style>
    /* Make buttons look bigger and nicer */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 50px;
        font-weight: bold;
        font-size: 16px;
    }
    /* Style for the green scan button */
    .scan-btn>button {
        background-color: #4CAF50 !important;
        color: white !important;
        border: none !important;
    }
    /* Style for the header */
    .header {
        background-color: #2b5797;
        color: white;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
        font-size: 24px;
        margin-bottom: 20px;
    }
    .red-text { color: #d9534f; font-weight: bold; font-size: 24px; text-align: center; }
    .small-text { color: gray; font-size: 14px; text-align: center; }
</style>
""", unsafe_allow_html=True)

# Initialize session state to track which screen we are on
if 'screen' not in st.session_state:
    st.session_state.screen = 'home'

# --- HOME SCREEN ---
if st.session_state.screen == 'home':
    st.markdown('<div class="header">MalariaXAI</div>', unsafe_allow_html=True)
    
    st.markdown("""
        <div style="border: 2px dashed #999; height: 250px; display: flex; align-items: center; justify-content: center; color: #999; margin-bottom: 20px;">
            [ camera view ]
        </div>
    """, unsafe_allow_html=True)
    
    # Interactive Buttons
    st.markdown('<div class="scan-btn">', unsafe_allow_html=True)
    if st.button("Scan smear"):
        st.session_state.screen = 'result'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("Choose from gallery"):
        st.info("Gallery feature will open here in the final app.")
        
    if st.button("History"):
        st.session_state.screen = 'history'
        st.rerun()
        
    st.markdown('<p class="small-text" style="color:#d9534f; margin-top: 30px;">Decision-support tool only</p>', unsafe_allow_html=True)

# --- RESULT SCREEN ---
elif st.session_state.screen == 'result':
    st.markdown('<div class="header">Result</div>', unsafe_allow_html=True)
    
    # Display your Grad-CAM image!
    # Replace 'heatmap.jpg' with your actual file if it has a different name
    try:
        st.image("heatmap.jpg", use_container_width=True)
    except:
        st.warning("⚠️ Please upload 'heatmap.jpg' to your GitHub repository to see the Grad-CAM here.")
        
    st.markdown('<div class="red-text">PARASITISED</div>', unsafe_allow_html=True)
    st.markdown('<p class="small-text">Confidence: 0.96 (example)<br>Time on phone: 0.4 s (example)</p>', unsafe_allow_html=True)
    st.markdown('<p class="small-text" style="color: #d9534f;">Red = region that drove the decision</p>', unsafe_allow_html=True)
    
    st.write("---")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Save"):
            st.success("Result saved to history!")
            st.session_state.screen = 'history'
            st.rerun()
    with col2:
        if st.button("Flag wrong"):
            st.warning("Result flagged for review.")
            
    if st.button("← Back to Home"):
        st.session_state.screen = 'home'
        st.rerun()

# --- HISTORY SCREEN ---
elif st.session_state.screen == 'history':
    st.markdown('<div class="header">History</div>', unsafe_allow_html=True)
    
    # Create a mock table
    history_data = [
        {"ID": "001", "Result": "Parasitised", "Conf": "0.97", "Highlight": False},
        {"ID": "002", "Result": "Uninfected", "Conf": "0.99", "Highlight": False},
        {"ID": "003", "Result": "Uninfected", "Conf": "0.62", "Highlight": True}, # Highlighted row
        {"ID": "004", "Result": "Parasitised", "Conf": "0.91", "Highlight": False},
        {"ID": "005", "Result": "Uninfected", "Conf": "0.95", "Highlight": False},
    ]
    
    for row in history_data:
        bg_color = "#fff3cd" if row["Highlight"] else "transparent"
        st.markdown(f"""
            <div style="display: flex; justify-content: space-between; padding: 15px; border-bottom: 1px solid #eee; background-color: {bg_color};">
                <span>{row['ID']}</span>
                <span>{row['Result']}</span>
                <span>{row['Conf']}</span>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown('<p class="small-text" style="text-align: left; margin-top: 20px; font-style: italic;">Highlighted row = flagged or low-confidence case for review</p>', unsafe_allow_html=True)
    
    st.write("---")
    if st.button("← Back to Home"):
        st.session_state.screen = 'home'
        st.rerun()
