import streamlit as st
import requests
from datetime import datetime
import json

st.set_page_config(
    page_title="Prompt Improver AI",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items=None
)

# Premium industry-grade CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        font-family: 'Poppins', sans-serif;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #0f172a 100%);
        color: #e2e8f0;
    }
    
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #0f172a 100%);
    }
    
    .main {
        background: transparent;
    }
    
    /* Header Section - Premium */
    .header-premium {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.95) 0%, rgba(51, 65, 85, 0.95) 50%, rgba(30, 41, 59, 0.95) 100%);
        padding: 70px 50px;
        border-radius: 20px;
        margin-bottom: 50px;
        text-align: center;
        border: 1px solid rgba(148, 163, 184, 0.15);
        box-shadow: 0 25px 80px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.1);
        animation: slideInDown 0.9s cubic-bezier(0.34, 1.56, 0.64, 1);
        position: relative;
        overflow: hidden;
    }
    
    .header-premium::before {
        content: '';
        position: absolute;
        top: -40%;
        right: -15%;
        width: 500px;
        height: 500px;
        background: radial-gradient(circle, rgba(59, 130, 246, 0.08) 0%, transparent 70%);
        border-radius: 50%;
    }
    
    .header-premium::after {
        content: '';
        position: absolute;
        bottom: -30%;
        left: -10%;
        width: 400px;
        height: 400px;
        background: radial-gradient(circle, rgba(139, 92, 246, 0.08) 0%, transparent 70%);
        border-radius: 50%;
    }
    
    .header-premium h1 {
        font-size: 56px;
        font-weight: 800;
        background: linear-gradient(135deg, #60a5fa 0%, #a78bfa 50%, #60a5fa 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 15px;
        animation: fadeInUp 0.9s ease-out;
        letter-spacing: -1px;
    }
    
    .header-premium p {
        font-size: 18px;
        color: #cbd5e1;
        animation: fadeInUp 1.1s ease-out;
        font-weight: 400;
        letter-spacing: 0.3px;
    }
    
    /* Input Sections */
    .input-section {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.8) 0%, rgba(51, 65, 85, 0.8) 100%);
        padding: 35px;
        border-radius: 16px;
        border: 1px solid rgba(148, 163, 184, 0.15);
        margin-bottom: 30px;
        box-shadow: 0 15px 50px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.05);
        animation: slideInUp 0.9s cubic-bezier(0.34, 1.56, 0.64, 1);
        backdrop-filter: blur(10px);
    }
    
    .section-title {
        font-size: 22px;
        font-weight: 700;
        color: #f1f5f9;
        margin-bottom: 25px;
        display: flex;
        align-items: center;
        gap: 12px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-size: 15px;
    }
    
    /* Text Area - Enhanced */
    .stTextArea > div > div > textarea {
        background: rgba(15, 23, 42, 0.6) !important;
        border: 2px solid rgba(100, 165, 230, 0.25) !important;
        border-radius: 12px !important;
        color: #e2e8f0 !important;
        font-size: 15px !important;
        padding: 18px !important;
        font-family: 'Inter', sans-serif !important;
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
        line-height: 1.6 !important;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #60a5fa !important;
        box-shadow: 0 0 30px rgba(96, 165, 250, 0.4), inset 0 0 10px rgba(96, 165, 250, 0.1) !important;
        background: rgba(15, 23, 42, 0.8) !important;
    }
    
    /* Checkboxes - Enhanced */
    .stCheckbox {
        padding: 12px 0;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    
    .stCheckbox:hover {
        background: rgba(96, 165, 250, 0.05);
        border-radius: 8px;
        padding-left: 8px;
    }
    
    .stCheckbox > label {
        color: #cbd5e1 !important;
        font-size: 15px !important;
        cursor: pointer !important;
        transition: all 0.3s ease;
        font-weight: 500;
    }
    
    .stCheckbox > label:hover {
        color: #60a5fa !important;
    }
    
    /* Button - Premium */
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 50%, #3b82f6 100%);
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 16px 45px !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        width: 100% !important;
        transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
        box-shadow: 0 15px 40px rgba(59, 130, 246, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.2) !important;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
        transition: left 0.5s;
    }
    
    .stButton > button:hover {
        transform: translateY(-4px) !important;
        box-shadow: 0 20px 50px rgba(59, 130, 246, 0.6) !important;
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
    .stButton > button:active {
        transform: translateY(-1px) !important;
    }
    
    /* Result Cards - Enhanced */
    .result-card {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.8) 0%, rgba(51, 65, 85, 0.8) 100%);
        padding: 30px;
        border-radius: 16px;
        border: 1px solid rgba(148, 163, 184, 0.15);
        min-height: 320px;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        box-shadow: 0 15px 50px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        animation: fadeIn 0.7s ease-out;
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    
    .result-card:hover {
        border-color: rgba(100, 165, 230, 0.35);
        box-shadow: 0 20px 60px rgba(59, 130, 246, 0.25), inset 0 1px 0 rgba(255, 255, 255, 0.1);
        transform: translateY(-2px);
    }
    
    .result-content {
        color: #cbd5e1;
        font-size: 15px;
        line-height: 1.8;
        font-family: 'Inter', sans-serif;
        word-wrap: break-word;
        overflow-y: auto;
        max-height: 350px;
        padding-right: 12px;
    }
    
    .result-content::-webkit-scrollbar {
        width: 8px;
    }
    
    .result-content::-webkit-scrollbar-track {
        background: rgba(100, 165, 230, 0.05);
        border-radius: 10px;
    }
    
    .result-content::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #3b82f6, #8b5cf6);
        border-radius: 10px;
        transition: all 0.3s ease;
    }
    
    .result-content::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #60a5fa, #a78bfa);
    }
    
    .placeholder-text {
        color: #64748b;
        font-style: italic;
        font-size: 15px;
    }
    
    /* Copy Button Container */
    .copy-button-container {
        margin-top: 20px;
        display: flex;
        gap: 10px;
        align-items: center;
    }
    
    .copy-btn {
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.9) 0%, rgba(16, 185, 129, 0.9) 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px 24px;
        font-weight: 600;
        font-size: 14px;
        cursor: pointer;
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        box-shadow: 0 10px 25px rgba(34, 197, 94, 0.3);
        text-transform: uppercase;
        letter-spacing: 0.5px;
        display: inline-flex;
        align-items: center;
        gap: 8px;
    }
    
    .copy-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 35px rgba(34, 197, 94, 0.5);
    }
    
    .copy-btn:active {
        transform: translateY(-1px);
    }
    
    .copy-feedback {
        color: #86efac;
        font-weight: 600;
        font-size: 14px;
        animation: fadeIn 0.3s ease-out;
    }
    
    /* Status Messages */
    .stSuccess {
        background: rgba(34, 197, 94, 0.1) !important;
        border: 1.5px solid rgba(34, 197, 94, 0.4) !important;
        border-radius: 12px !important;
        padding: 18px !important;
        color: #86efac !important;
        animation: slideInDown 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
        font-weight: 500;
    }
    
    .stError {
        background: rgba(239, 68, 68, 0.1) !important;
        border: 1.5px solid rgba(239, 68, 68, 0.4) !important;
        border-radius: 12px !important;
        padding: 18px !important;
        color: #fca5a5 !important;
        animation: slideInDown 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
        font-weight: 500;
    }
    
    .stWarning {
        background: rgba(251, 191, 36, 0.1) !important;
        border: 1.5px solid rgba(251, 191, 36, 0.4) !important;
        border-radius: 12px !important;
        padding: 18px !important;
        color: #fde047 !important;
        font-weight: 500;
    }
    
    .stInfo {
        background: rgba(59, 130, 246, 0.1) !important;
        border: 1.5px solid rgba(59, 130, 246, 0.4) !important;
        border-radius: 12px !important;
        padding: 18px !important;
        color: #93c5fd !important;
        font-weight: 500;
    }
    
    /* Code Block */
    .stCode {
        background: rgba(15, 23, 42, 0.8) !important;
        border: 1px solid rgba(100, 165, 230, 0.2) !important;
        border-radius: 12px !important;
        padding: 20px !important;
    }
    
    /* Animations */
    @keyframes slideInDown {
        from {
            opacity: 0;
            transform: translateY(-40px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes slideInUp {
        from {
            opacity: 0;
            transform: translateY(40px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }
    
    .pulse {
        animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
    }
    
    /* Divider */
    hr {
        background: linear-gradient(90deg, transparent, rgba(148, 163, 184, 0.15), transparent);
        border: none;
        height: 1px;
        margin: 50px 0;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: #64748b;
        font-size: 14px;
        padding: 40px 0;
        border-top: 1px solid rgba(148, 163, 184, 0.1);
        margin-top: 50px;
    }
    
    .footer p {
        margin: 10px 0;
        font-weight: 400;
        letter-spacing: 0.3px;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="header-premium">
        <h1>✨ Prompt Improver AI</h1>
        <p>Professional-Grade Prompt Enhancement & Optimization Engine</p>
    </div>
""", unsafe_allow_html=True)

# Input Section
st.markdown('<div class="input-section">', unsafe_allow_html=True)
st.markdown('<div class="section-title">📝 Your Prompt</div>', unsafe_allow_html=True)
user_input = st.text_area(
    "Enter or paste your prompt:",
    height=130,
    placeholder="Type or paste your prompt here to begin enhancement...",
    label_visibility="collapsed"
)
st.markdown('</div>', unsafe_allow_html=True)

# Techniques Section
st.markdown('<div class="input-section">', unsafe_allow_html=True)
st.markdown('<div class="section-title">🎯 Enhancement Methods</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    be_specific = st.checkbox("📌 Be Specific - Add Details & Constraints")
    role = st.checkbox("👤 Assign Role - Define AI Purpose")
    few_shot = st.checkbox("📚 Few-Shot Examples - Provide References")

with col2:
    cot = st.checkbox("🧠 Chain of Thought - Enable Reasoning")
    format_def = st.checkbox("📋 Define Format - Specify Output Structure")

techniques = []
if be_specific:
    techniques.append("Be specific (add details and constraints)")
if role:
    techniques.append("Give a role (assign AI a role)")
if few_shot:
    techniques.append("Few-shot examples")
if cot:
    techniques.append("Chain of thought reasoning")
if format_def:
    techniques.append("Define output format")

st.markdown('</div>', unsafe_allow_html=True)

# Results Section
st.markdown('<hr>', unsafe_allow_html=True)

col_left, col_right = st.columns(2, gap="large")

improved_text = ""

with col_left:
    st.markdown('<div class="section-title">📄 Original Prompt</div>', unsafe_allow_html=True)
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="result-content">{user_input if user_input.strip() else "<span class=\'placeholder-text\'>Your original prompt will appear here...</span>"}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    st.markdown('<div class="section-title">✨ Enhanced Prompt</div>', unsafe_allow_html=True)
    
    if st.button("🚀 ENHANCE PROMPT NOW", use_container_width=True):
        if not user_input.strip():
            st.warning("⚠️ Please enter a prompt to enhance!")
        else:
            with st.spinner("⚡ Processing your prompt..."):
                try:
                    res = requests.post(
                        "http://127.0.0.1:8000/api/v1/prompts/improve",
                        json={
                            "prompt": user_input,
                            "techniques": ", ".join(techniques) if techniques else ""
                        },
                        timeout=30
                    )
                    
                    if res.status_code == 200:
                        result = res.json()
                        
                        if "status" in result and result["status"] == "error":
                            st.error(f"❌ API Error: {result.get('message', 'Unknown error')}")
                        else:
                            improved_text = result.get("improved_prompt", "")
                            st.markdown('<div class="result-card">', unsafe_allow_html=True)
                            st.markdown(f'<div class="result-content">{improved_text}</div>', unsafe_allow_html=True)
                            st.markdown('</div>', unsafe_allow_html=True)
                            
                            # Copy Button with functionality
                            st.markdown("""
                                <div class="copy-button-container">
                            """, unsafe_allow_html=True)
                            
                            col_copy_1, col_copy_2 = st.columns([1, 3])
                            
                            with col_copy_1:
                                if st.button("📋 Copy", key="copy_btn", use_container_width=True):
                                    # Create JavaScript to copy to clipboard
                                    st.write("""
                                        <script>
                                        function copyToClipboard() {
                                            const text = `""" + improved_text.replace('"', '\\"').replace('\n', '\\n') + """`;
                                            navigator.clipboard.writeText(text).then(() => {
                                                alert('✅ Copied to clipboard!');
                                            });
                                        }
                                        copyToClipboard();
                                        </script>
                                    """, unsafe_allow_html=True)
                            
                            st.markdown('</div>', unsafe_allow_html=True)
                            
                            st.success("✅ Prompt enhanced successfully!")
                            
                            st.markdown('<br>', unsafe_allow_html=True)
                            st.markdown('#### 📋 Copy Your Enhanced Prompt')
                            st.code(improved_text, language="text")
                    else:
                        st.error(f"❌ Server Error {res.status_code}")
                
                except requests.exceptions.Timeout:
                    st.error("⏱️ Request timeout - server took too long")
                except requests.exceptions.ConnectionError:
                    st.error("🔌 Cannot reach backend → http://127.0.0.1:8000 not responding")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
    else:
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown('<div class="result-content"><span class="placeholder-text">Your enhanced prompt will appear here after processing...</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <p>⚡ Powered by Groq AI - Lightning Fast Processing</p>
        <p>🔒 Enterprise-Grade Security | 🚀 Industry Standard | ✨ Production Ready</p>
    </div>
""", unsafe_allow_html=True)