import streamlit as st
import time
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="FocusGrid Console", layout="wide")

# 🎨 Injected 3D CSS Shadows & Styles (Error-Proof Rendering)
st.markdown("""
    <style>
    .stApp { background-color: #0A0D14; }
    
    /* Tactile 3D Soft Neumorphic Card */
    .clay-card {
        background: #121824;
        border-radius: 24px;
        padding: 35px;
        text-align: center;
        box-shadow: 10px 10px 20px #040609, -6px -6px 15px #202a3f;
        border: 1px solid rgba(255, 255, 255, 0.02);
        margin-bottom: 25px;
    }
    
    /* 3D Co-worker Badge Node */
    .user-node {
        background: #1A2333;
        border-radius: 16px;
        padding: 15px;
        text-align: center;
        box-shadow: 5px 5px 10px #05070a, -3px -3px 8px #222e44;
        border-left: 4px solid #8B5CF6;
        color: white;
    }
    
    /* Glowing Non-Distracting Flow Anchor */
    .pulse-indicator {
        width: 100px;
        height: 100px;
        background: radial-gradient(circle, #8B5CF6 0%, #3B82F6 100%);
        border-radius: 50%;
        margin: 30px auto;
        box-shadow: 0 0 30px rgba(139, 92, 246, 0.5);
        animation: breath 4s infinite ease-in-out;
    }
    
    @keyframes breath {
        0% { transform: scale(0.95); opacity: 0.8; }
        50% { transform: scale(1.05); opacity: 1; box-shadow: 0 0 50px rgba(59, 130, 246, 0.7); }
        100% { transform: scale(0.95); opacity: 0.8; }
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white; font-weight: 800;'>🎮 FocusGrid Workspace</h1>", unsafe_allow_html=True)

if "in_flow" not in st.session_state:
    st.session_state.in_flow = False

# Layout split
left_col, right_col = st.columns([1, 1.5])

with left_col:
    st.markdown("<div class='clay-card'>", unsafe_allow_html=True)
    if not st.session_state.in_flow:
        st.markdown("<h3 style='color: white; margin-top:0;'>Lock in Session</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color: #64748B; font-size:14px;'>Enter the zone silently with your peers.</p>", unsafe_allow_html=True)
        
        track = st.selectbox("Select Study Node", ["Core Architecture", "Compiler Engineering", "Data Structures"])
        
        if st.button("🚀 Enter Flow State", use_container_width=True):
            st.session_state.in_flow = True
            st.session_state.start_time = time.time()
            st.rerun()
    else:
        st.markdown("<h3 style='color: white; margin-top:0;'>✨ In The Zone</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color: #94A3B8; font-size:14px;'>No clock ticking anxiety. Stay focused.</p>", unsafe_allow_html=True)
        st.markdown("<div class='pulse-indicator'></div>", unsafe_allow_html=True)
        
        if st.button("🚪 Leave & Claim XP", use_container_width=True):
            duration = round((time.time() - st.session_state.start_time) / 60, 2)
            st.session_state.in_flow = False
            st.success(f"Focused for {duration} minutes! Data saved.")
    st.markdown("</div>", unsafe_allow_html=True)

with right_col:
    st.markdown("<div class='clay-card'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white; margin-top:0; text-align:left;'>📈 Campus Peak Flow Volume</h3>", unsafe_allow_html=True)
    
    # Live analytical layout mapping
    df = pd.DataFrame({"Hour": ["08:00", "11:00", "14:00", "17:00", "20:00"], "Students Active": [15, 54, 42, 88, 110]})
    fig = px.line(df, x="Hour", y="Students Active", template="plotly_dark")
    fig.update_traces(line_color='#8B5CF6', line_width=4)
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=10, r=10, t=10, b=10))
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 👥 Shared Social Presence Accountability Grid
st.markdown("<h3 style='color: white; text-align: center;'>👥 Active Co-Workers in Your Node</h3>", unsafe_allow_html=True)
g1, g2, g3, g4 = st.columns(4)
with g1: st.markdown("<div class='user-node'><strong>👨‍💻 Rahul K.</strong><br><span style='color:#64748B; font-size:12px;'>Focusing for 45m</span></div>", unsafe_allow_html=True)
with g2: st.markdown("<div class='user-node' style='border-left-color:#3B82F6;'><strong>👩‍💻 Priya M.</strong><br><span style='color:#64748B; font-size:12px;'>Focusing for 22m</span></div>", unsafe_allow_html=True)
with g3: st.markdown("<div class='user-node'><strong>👨‍💻 Amit S.</strong><br><span style='color:#64748B; font-size:12px;'>Focusing for 61m</span></div>", unsafe_allow_html=True)
with g4: st.markdown("<div class='user-node' style='border-left-color:#3B82F6;'><strong>👩‍💻 Sneha R.</strong><br><span style='color:#64748B; font-size:12px;'>Focusing for 12m</span></div>", unsafe_allow_html=True)