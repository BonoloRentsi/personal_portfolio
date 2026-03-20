import streamlit as st
from datetime import datetime
import json

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="BBBBBBBBBBB | Data Scientist",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.example.com',
        'Report a bug': "https://www.example.com",
        'About': "### Portfolio v2.0\nBuilt with Streamlit"
    }
)

# -----------------------------
# SESSION STATE INITIALIZATION
# -----------------------------
if 'contact_submissions' not in st.session_state:
    st.session_state.contact_submissions = []
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

# -----------------------------
# ENHANCED GLOBAL CSS
# -----------------------------
st.markdown("""
<style>
* { 
    font-family: 'Poppins', 'Segoe UI', 'Segoe UI Emoji', sans-serif; 
    transition: background-color 0.3s ease, color 0.3s ease;
}

:root {
    --primary: #667eea;
    --secondary: #764ba2;
    --accent: #f59e0b;
    --light: #f8fafc;
    --dark: #1e293b;
    --card-light: #ffffff;
    --card-dark: #2d3748;
}

.dark-mode {
    background-color: #0f172a;
    color: #e2e8f0;
}

.dark-mode .card {
    background-color: var(--card-dark);
    color: #e2e8f0;
    border-left-color: var(--accent);
}

.dark-mode .tag {
    background: linear-gradient(135deg, #4a5568 0%, #2d3748 100%);
    color: #cbd5e1;
    border-color: #4a5568;
}

.dark-mode h1, .dark-mode h2, .dark-mode h3 {
    color: #f1f5f9;
}

body { 
    background-color: var(--light); 
    color: var(--dark);
    min-height: 100vh;
}

h1, h2, h3 { 
    color: var(--dark); 
    font-weight: 600; 
    line-height: 1.2;
}
h1 { 
    font-size: 2.8rem; 
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
}
h2 { 
    border-bottom: 3px solid var(--primary); 
    padding-bottom: 10px; 
    margin-top: 40px; 
    font-size: 1.9rem; 
    position: relative;
}
h2:after {
    content: '';
    position: absolute;
    bottom: -3px;
    left: 0;
    width: 60px;
    height: 3px;
    background: var(--accent);
}
h3 { 
    font-size: 1.5rem; 
    margin-bottom: 12px;
    color: var(--primary);
}

.card { 
    background-color: var(--card-light);  
    color: var(--dark);
    padding: 28px; 
    border-radius: 16px; 
    box-shadow: 0 8px 30px rgba(0,0,0,0.08); 
    margin-bottom: 28px; 
    border-left: 5px solid var(--primary); 
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.1); 
    height: 100%;
    border-top: 1px solid rgba(102, 126, 234, 0.1);
}
.card:hover { 
    transform: translateY(-5px) scale(1.01); 
    box-shadow: 0 20px 40px rgba(0,0,0,0.15); 
    border-left-color: var(--accent);
}

.tag { 
    display: inline-block; 
    background: linear-gradient(135deg, #e0e7ff 0%, #c7d2fe 100%); 
    color: #4c51bf; 
    padding: 6px 16px; 
    border-radius: 50px; 
    margin: 5px 8px 5px 0; 
    font-size: 0.85rem; 
    font-weight: 600; 
    border: 1px solid #c3dafe; 
    transition: all 0.3s ease; 
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}
.tag:hover { 
    background: linear-gradient(135deg, #c7d2fe 0%, #a5b4fc 100%); 
    transform: translateY(-2px); 
    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.2);
}

.project-title { 
    color: var(--primary); 
    font-weight: 700; 
    margin-bottom: 8px; 
    font-size: 1.4rem;
    display: flex;
    align-items: center;
    gap: 10px;
}
.project-title:before {
    content: "▸";
    color: var(--accent);
    font-size: 1.2em;
}

.custom-btn { 
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%); 
    color: white; 
    padding: 12px 24px; 
    border-radius: 10px; 
    text-decoration: none; 
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    margin: 8px 8px 8px 0; 
    border: none; 
    cursor: pointer; 
    font-weight: 600; 
    transition: all 0.3s ease; 
    text-align: center;
    box-shadow: 0 4px 14px rgba(102, 126, 234, 0.3);
    min-width: 140px;
}
.custom-btn:hover { 
    transform: translateY(-3px); 
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4); 
    color: white; 
    text-decoration: none;
}

.stTextInput > div > div > input,
.stTextArea > div > div > textarea { 
    border-radius: 10px; 
    border: 2px solid #e0e0e0; 
    padding: 14px; 
    font-size: 1rem;
    transition: all 0.3s ease;
    background-color: #f8fafc;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus { 
    border-color: var(--primary); 
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.2);
    background-color: white;
}

.stButton > button { 
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%); 
    color: white; 
    border: none; 
    padding: 14px 32px; 
    border-radius: 10px; 
    font-weight: 600; 
    transition: all 0.3s ease; 
    width: 100%; 
    font-size: 1.05rem;
    position: relative;
    overflow: hidden;
}
.stButton > button:hover { 
    transform: translateY(-3px); 
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
}
.stButton > button:after {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 5px;
    height: 5px;
    background: rgba(255, 255, 255, 0.5);
    opacity: 0;
    border-radius: 100%;
    transform: scale(1, 1) translate(-50%);
    transform-origin: 50% 50%;
}
.stButton > button:focus:not(:active)::after {
    animation: ripple 1s ease-out;
}

.main-header { 
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%); 
    padding: 50px 20px; 
    border-radius: 0 0 25px 25px; 
    margin-bottom: 40px; 
    color: white; 
    text-align: center;
    position: relative;
    overflow: hidden;
}
.main-header:before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: url("data:image/svg+xml,%3Csvg width='100' height='100' viewBox='0 0 100 100' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M11 18c3.866 0 7-3.134 7-7s-3.134-7-7-7-7 3.134-7 7 3.134 7 7 7zm48 25c3.866 0 7-3.134 7-7s-3.134-7-7-7-7 3.134-7 7 3.134 7 7 7zm-43-7c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zm63 31c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zM34 90c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zm56-76c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zM12 86c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm28-65c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm23-11c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm-6 60c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm29 22c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zM32 63c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm57-13c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm-9-21c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zM60 91c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zM35 41c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zM12 60c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2z' fill='%23ffffff' fill-opacity='0.05' fill-rule='evenodd'/%3E%3C/svg%3E");
}
.main-header h1 { 
    color: white; 
    font-size: 3.2rem; 
    margin-bottom: 15px; 
    font-weight: 700;
    text-shadow: 0 2px 10px rgba(0,0,0,0.1);
    position: relative;
}
.main-header p { 
    font-size: 1.3rem; 
    opacity: 0.95; 
    font-weight: 300;
    position: relative;
}

.typing-text {
    display: inline-block;
    overflow: hidden;
    border-right: 3px solid white;
    white-space: nowrap;
    animation: typing 3.5s steps(40, end), blink-caret 0.75s step-end infinite;
}

@keyframes typing {
    from { width: 0 }
    to { width: 100% }
}

@keyframes blink-caret {
    from, to { border-color: transparent }
    50% { border-color: white; }
}

@keyframes ripple {
    0% {
        transform: scale(0, 0);
        opacity: 1;
    }
    20% {
        transform: scale(25, 25);
        opacity: 1;
    }
    100% {
        opacity: 0;
        transform: scale(40, 40);
    }
}

.progress-bar {
    height: 8px;
    background: linear-gradient(90deg, var(--primary), var(--secondary));
    border-radius: 4px;
    margin-top: 5px;
    margin-bottom: 15px;
}

.stats-card {
    text-align: center;
    padding: 20px;
    background: linear-gradient(135deg, #f8fafc 0%, #e0e7ff 100%);
    border-radius: 12px;
    border: 2px solid #e0e7ff;
}

.stats-number {
    font-size: 2.5rem;
    font-weight: 700;
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.stats-label {
    font-size: 0.9rem;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: 600;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Dark mode toggle */
.dark-toggle {
    position: fixed;
    top: 20px;
    right: 20px;
    z-index: 1000;
}
</style>
""", unsafe_allow_html=True)

# Apply dark mode if enabled
if st.session_state.dark_mode:
    st.markdown('<div class="dark-mode">', unsafe_allow_html=True)

# -----------------------------
# DARK MODE TOGGLE
# -----------------------------
col1, col2, col3 = st.columns([6, 2, 2])
with col3:
    if st.button("🌙 Dark Mode" if not st.session_state.dark_mode else "☀️ Light Mode", key="dark_mode_toggle"):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()

# -----------------------------
# CV DATA (Enhanced with JSON)
# -----------------------------
cv_data = {
    "name": "BBBBBBBBBBB",
    "title": "Data Scientist",
    "contact": {
        "email": "HELLO@gmail.com",
        "phone": "+27 000 000 0000",
        "location": "Kimberley, South Africa"
    },
    "education": [
        {
            "degree": "BSc Computer Science/Data Science",
            "institution": "Sol Plaatje University",
            "period": "2022-2025",
            "details": ["GPA: 3.8/4.0", "Specialization in Machine Learning"]
        }
    ],
    "skills": {
        "Programming": ["Python", "R", "SQL", "C++"],
        "Data Science": ["Machine Learning", "Deep Learning", "Data Visualization", "NLP"],
        "Tools": ["Tableau", "PowerBI", "Git", "GitHub", "Docker", "AWS"]
    }
}

# -----------------------------
# HEADER
# -----------------------------
st.markdown(f"""
<div class="main-header">
    <h1>{cv_data['name']}</h1>
    <p class="typing-text">Data Scientist | AI Enthusiast | Problem Solver</p>
    <div style="margin-top: 30px; display: flex; gap: 15px; justify-content: center; flex-wrap: wrap;">
        <a href="mailto:{cv_data['contact']['email']}" class="custom-btn">📧 Email</a>
        <a href="https://github.com/username" target="_blank" class="custom-btn">🐙 GitHub</a>
        <a href="https://www.kaggle.com/username" target="_blank" class="custom-btn">📊 Kaggle</a>
        <a href="https://linkedin.com/in/username" target="_blank" class="custom-btn">💼 LinkedIn</a>
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# STATS BAR
# -----------------------------
st.markdown("### 📈 Quick Stats")
stats_cols = st.columns(4)
with stats_cols[0]:
    st.markdown("""
    <div class="stats-card">
        <div class="stats-number">3+</div>
        <div class="stats-label">Years Experience</div>
    </div>
    """, unsafe_allow_html=True)
with stats_cols[1]:
    st.markdown("""
    <div class="stats-card">
        <div class="stats-number">15+</div>
        <div class="stats-label">Projects</div>
    </div>
    """, unsafe_allow_html=True)
with stats_cols[2]:
    st.markdown("""
    <div class="stats-card">
        <div class="stats-number">10+</div>
        <div class="stats-label">Technologies</div>
    </div>
    """, unsafe_allow_html=True)
with stats_cols[3]:
    st.markdown("""
    <div class="stats-card">
        <div class="stats-number">98%</div>
        <div class="stats-label">Satisfaction</div>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# TABS
# -----------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠 ABOUT", "📄 RESUME", "💼 PROJECTS", "🔧 SKILLS", "📱 CONTACT"])

# -----------------------------
# ABOUT ME
# -----------------------------
with tab1:
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("<h2>👋 About Me</h2>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class='card'>
            <p>Hello! I'm <strong>{cv_data['name']}</strong>, a passionate Data Scientist with a strong background in transforming complex data into actionable insights.</p>
            
            <p>🔹 With expertise in <strong>Python, R, SQL</strong>, and advanced <strong>Machine Learning</strong> techniques</p>
            <p>🔹 Proven track record in delivering <strong>end-to-end data solutions</strong></p>
            <p>🔹 Specialized in <strong>Computer Vision, NLP, and Predictive Analytics</strong></p>
            <p>🔹 Committed to <strong>clean code, best practices, and continuous learning</strong></p>
            
            <div style='margin-top: 20px; padding: 15px; background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); border-radius: 10px;'>
                <strong>🎯 Currently seeking:</strong> Data Scientist/Analyst roles | ML Engineer positions | Research Opportunities
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("<h2>🎯 Core Values</h2>", unsafe_allow_html=True)
        st.markdown("""
        <div class='card'>
            <div style='display: flex; align-items: center; margin-bottom: 15px;'>
                <span style='font-size: 1.5rem; margin-right: 10px;'>💡</span>
                <div>
                    <strong>Innovation</strong><br>
                    <small>Embracing new technologies</small>
                </div>
            </div>
            <div style='display: flex; align-items: center; margin-bottom: 15px;'>
                <span style='font-size: 1.5rem; margin-right: 10px;'>🎯</span>
                <div>
                    <strong>Precision</strong><br>
                    <small>Data-driven accuracy</small>
                </div>
            </div>
            <div style='display: flex; align-items: center; margin-bottom: 15px;'>
                <span style='font-size: 1.5rem; margin-right: 10px;'>🤝</span>
                <div>
                    <strong>Collaboration</strong><br>
                    <small>Team-oriented approach</small>
                </div>
            </div>
            <div style='display: flex; align-items: center;'>
                <span style='font-size: 1.5rem; margin-right: 10px;'>📈</span>
                <div>
                    <strong>Growth</strong><br>
                    <small>Continuous learning mindset</small>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<h2>🌟 What I Offer</h2>", unsafe_allow_html=True)
    offer_cols = st.columns(3)
    offers = [
        {"icon": "🤖", "title": "AI Solutions", "desc": "Custom ML/DL models for real-world problems"},
        {"icon": "📊", "title": "Data Insights", "desc": "Actionable business intelligence from data"},
        {"icon": "🚀", "title": "End-to-End", "desc": "Full project lifecycle development"}
    ]
    
    for col, offer in zip(offer_cols, offers):
        with col:
            st.markdown(f"""
            <div class='card' style='text-align: center;'>
                <div style='font-size: 3rem; margin-bottom: 15px;'>{offer['icon']}</div>
                <h3 style='color: var(--primary);'>{offer['title']}</h3>
                <p>{offer['desc']}</p>
            </div>
            """, unsafe_allow_html=True)

# -----------------------------
# RESUME
# -----------------------------
with tab2:
    st.markdown("<h2>🎓 Education</h2>", unsafe_allow_html=True)
    
    edu_cols = st.columns(2)
    educations = [
        {
            "title": "BSc Computer Science (Data Science)",
            "institution": "Sol Plaatje University",
            "period": "Jan 2022 - Dec 2024",
            "gpa": "81% Average",
            "details": ["Machine Learning Specialization", "Data Engineering", "Statistics & Probability"]
        },
        {
            "title": "BSc Honours (Computer Sciences)",
            "institution": "Sol Plaatje University",
            "period": "Jan 2025 - Present",
            "gpa": "78% Average",
            "details": ["Advanced AI Research", "Big Data Analytics", "Research Methodology"]
        }
    ]
    
    for col, edu in zip(edu_cols, educations):
        with col:
            details_html = "".join([f"<li>{d}</li>" for d in edu["details"]])
            st.markdown(f"""
            <div class='card'>
                <h3>{edu['title']}</h3>
                <p><strong>{edu['institution']}</strong> | {edu['period']}</p>
                <div class='progress-bar' style='width: {edu['gpa'].split('%')[0]}%;'></div>
                <p><strong>Performance:</strong> {edu['gpa']}</p>
                <ul>{details_html}</ul>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<h2>💼 Experience</h2>", unsafe_allow_html=True)
    
    experiences = [
        {
            "title": "Peer Mentor",
            "company": "Sol Plaatje University",
            "period": "Jan 2025 - Present",
            "achievements": [
                "Provided academic guidance to 50+ students",
                "Improved student retention by 15%",
                "Developed study materials and workshops"
            ]
        },
        {
            "title": "Academic Support Specialist",
            "company": "Sol Plaatje University",
            "period": "Jan 2025 - Present",
            "achievements": [
                "Tutored 100+ hours in data science courses",
                "Created interactive learning resources",
                "Mentored 20+ students in research projects"
            ]
        },
        {
            "title": "Teaching Assistant",
            "company": "Homevale High School",
            "period": "Jan 2023 - Dec 2023",
            "achievements": [
                "Assisted in STEM curriculum development",
                "Tutored 30+ students in computer science",
                "Implemented digital learning tools"
            ]
        }
    ]
    
    for exp in experiences:
        achievements_html = "".join([f"<li>{a}</li>" for a in exp["achievements"]])
        st.markdown(f"""
        <div class='card'>
            <div style='display: flex; justify-content: space-between; align-items: start;'>
                <div>
                    <h3>{exp['title']}</h3>
                    <p><strong>{exp['company']}</strong></p>
                </div>
                <span style='background: linear-gradient(135deg, var(--primary), var(--secondary)); color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem;'>
                    {exp['period']}
                </span>
            </div>
            <ul>{achievements_html}</ul>
        </div>
        """, unsafe_allow_html=True)

# -----------------------------
# PROJECTS
# -----------------------------
with tab3:
    st.markdown("<h2>🚀 Featured Projects</h2>", unsafe_allow_html=True)
    
    projects = [
        {
            "title": "Skin Disease Detection",
            "description": "CNN-based model for classifying skin diseases with 94% accuracy",
            "tags": ["Python", "TensorFlow", "CNN", "OpenCV", "Flask"],
            "github": "https://github.com/username/skin-disease",
            "kaggle": "https://www.kaggle.com/username/skin-disease",
            "status": "Completed"
        },
        {
            "title": "Network Traffic Analysis",
            "description": "Real-time anomaly detection system for network security",
            "tags": ["Python", "Scikit-learn", "Streamlit", "ML", "Cybersecurity"],
            "github": "https://github.com/username/network-traffic",
            "kaggle": "https://www.kaggle.com/username/network-traffic",
            "status": "Active"
        },
        {
            "title": "Breast Cancer Classification",
            "description": "Predictive model with 97% accuracy using ensemble methods",
            "tags": ["Python", "XGBoost", "Feature Engineering", "SHAP"],
            "github": "https://github.com/username/breast-cancer",
            "kaggle": "https://www.kaggle.com/username/breast-cancer",
            "status": "Completed"
        },
        {
            "title": "University Chatbot",
            "description": "AI-powered chatbot for student queries using NLP",
            "tags": ["Python", "NLTK", "Transformers", "FastAPI", "Docker"],
            "github": "https://github.com/username/university-chatbot",
            "kaggle": "https://www.kaggle.com/username/university-chatbot",
            "status": "In Progress"
        }
    ]
    
    for project in projects:
        tags_html = " ".join([f"<span class='tag'>{t}</span>" for t in project['tags']])
        status_color = "#10b981" if project['status'] == "Completed" else "#f59e0b" if project['status'] == "Active" else "#6366f1"
        
        st.markdown(f"""
        <div class='card'>
            <div style='display: flex; justify-content: space-between; align-items: start;'>
                <h3 class='project-title'>{project['title']}</h3>
                <span style='background-color: {status_color}; color: white; padding: 3px 10px; border-radius: 15px; font-size: 0.8rem;'>
                    {project['status']}
                </span>
            </div>
            <p>{project['description']}</p>
            {tags_html}
            <div style='margin-top: 20px; display: flex; gap: 10px;'>
                <a href='{project['github']}' target='_blank' class='custom-btn'>🐙 View Code</a>
                <a href='{project['kaggle']}' target='_blank' class='custom-btn'>📊 Kaggle</a>
                <button class='custom-btn' onclick='alert("Demo coming soon!")'>🎬 Demo</button>
            </div>
        </div>
        """, unsafe_allow_html=True)

# -----------------------------
# SKILLS
# -----------------------------
with tab4:
    st.markdown("<h2>🔧 Technical Skills</h2>", unsafe_allow_html=True)
    
    skills_categories = {
        "Programming": ["Python (Expert)", "R (Advanced)", "SQL (Advanced)", "C++ (Intermediate)"],
        "Data Science": ["Machine Learning", "Deep Learning", "NLP", "Computer Vision", "Statistical Analysis"],
        "Data Tools": ["Pandas", "NumPy", "Scikit-learn", "TensorFlow", "PyTorch"],
        "Visualization": ["Tableau", "Power BI", "Matplotlib", "Seaborn", "Plotly"],
        "DevOps": ["Git", "Docker", "AWS", "CI/CD", "Linux"],
        "Databases": ["MySQL", "PostgreSQL", "MongoDB", "SQLite"]
    }
    
    for category, skills in skills_categories.items():
        st.markdown(f"<h3>{category}</h3>", unsafe_allow_html=True)
        skills_html = " ".join([f"<span class='tag' style='font-size: 1rem; padding: 8px 20px;'>{s}</span>" for s in skills])
        st.markdown(f"<div style='margin-bottom: 30px;'>{skills_html}</div>", unsafe_allow_html=True)
    
    st.markdown("<h2>📈 Skill Proficiency</h2>", unsafe_allow_html=True)
    
    proficiency = {
        "Python": 95,
        "Machine Learning": 90,
        "SQL": 85,
        "Data Visualization": 88,
        "Deep Learning": 82
    }
    
    for skill, level in proficiency.items():
        st.markdown(f"""
        <div style='margin-bottom: 20px;'>
            <div style='display: flex; justify-content: space-between; margin-bottom: 5px;'>
                <span><strong>{skill}</strong></span>
                <span>{level}%</span>
            </div>
            <div class='progress-bar' style='width: {level}%;'></div>
        </div>
        """, unsafe_allow_html=True)

# -----------------------------
# CONTACT
# -----------------------------
with tab5:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<h2>📱 Contact Information</h2>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class='card'>
            <div style='display: flex; align-items: center; margin-bottom: 20px;'>
                <span style='font-size: 2rem; margin-right: 15px;'>📧</span>
                <div>
                    <strong>Email</strong><br>
                    <a href='mailto:{cv_data['contact']['email']}'>{cv_data['contact']['email']}</a>
                </div>
            </div>
            <div style='display: flex; align-items: center; margin-bottom: 20px;'>
                <span style='font-size: 2rem; margin-right: 15px;'>📱</span>
                <div>
                    <strong>Phone</strong><br>
                    {cv_data['contact']['phone']}
                </div>
            </div>
            <div style='display: flex; align-items: center; margin-bottom: 20px;'>
                <span style='font-size: 2rem; margin-right: 15px;'>📍</span>
                <div>
                    <strong>Location</strong><br>
                    {cv_data['contact']['location']}
                </div>
            </div>
            <div style='margin-top: 30px; display: flex; gap: 10px; flex-wrap: wrap;'>
                <a href='mailto:{cv_data['contact']['email']}' class='custom-btn'>📧 Email Me</a>
                <a href='https://github.com/username' target='_blank' class='custom-btn'>🐙 GitHub</a>
                <a href='https://linkedin.com/in/username' target='_blank' class='custom-btn'>💼 LinkedIn</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("<h2>✉️ Send Message</h2>", unsafe_allow_html=True)
        
        with st.form("contact_form", clear_on_submit=True):
            col_a, col_b = st.columns(2)
            with col_a:
                name = st.text_input("Name *", placeholder="Your full name")
            with col_b:
                email = st.text_input("Email *", placeholder="you@example.com")
            
            subject = st.selectbox(
                "Subject *",
                ["", "Project Inquiry", "Job Opportunity", "Collaboration", "Question", "Other"]
            )
            
            message = st.text_area("Message *", height=150, placeholder="Your message here...")
            
            submitted = st.form_submit_button("📨 Send Message", use_container_width=True)
            
            if submitted:
                if name and email and subject and message:
                    # Store submission
                    submission = {
                        "name": name,
                        "email": email,
                        "subject": subject,
                        "message": message,
                        "timestamp": datetime.now().isoformat()
                    }
                    st.session_state.contact_submissions.append(submission)
                    
                    # Success message
                    st.success(f"✅ Thank you {name}! Your message has been sent successfully.")
                    st.balloons()
                    
                    # Display confirmation
                    with st.expander("📋 Message Preview"):
                        st.write(f"**From:** {name}")
                        st.write(f"**Email:** {email}")
                        st.write(f"**Subject:** {subject}")
                        st.write(f"**Message:** {message}")
                else:
                    st.warning("⚠️ Please fill in all required fields (*)")

# Close dark mode div if enabled
if st.session_state.dark_mode:
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; padding: 40px 0; color: #666;">
    <p style="font-size: 1.1rem; margin-bottom: 10px;">
        <strong>{cv_data['name']}</strong> | {cv_data['title']}
    </p>
    <p style="font-size: 0.9rem; opacity: 0.8; margin-bottom: 20px;">
        {cv_data['contact']['location']} | {cv_data['contact']['email']}
    </p>
    <div style="display: flex; justify-content: center; gap: 20px; margin-bottom: 20px;">
        <a href="mailto:{cv_data['contact']['email']}" style="color: #666; text-decoration: none;">📧 Email</a>
        <a href="https://github.com/username" target="_blank" style="color: #666; text-decoration: none;">🐙 GitHub</a>
        <a href="https://linkedin.com/in/username" target="_blank" style="color: #666; text-decoration: none;">💼 LinkedIn</a>
        <a href="https://kaggle.com/username" target="_blank" style="color: #666; text-decoration: none;">📊 Kaggle</a>
    </div>
    <p style="font-size: 0.8rem; opacity: 0.6;">
        © {datetime.now().year} | Built with ❤️ using Streamlit | v2.0 | Last updated: {datetime.now().strftime('%B %d, %Y')}
    </p>
</div>
""", unsafe_allow_html=True)