import streamlit as st
from datetime import datetime

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Portfolio | Data Scientist",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────
if "contact_submissions" not in st.session_state:
    st.session_state.contact_submissions = []

# ─────────────────────────────────────────────
# DATA
# ─────────────────────────────────────────────
cv_data = {
    "name": "BBBBBBB",
    "initials": "BARBBB",
    "title": "Data Scientist",
    "tagline": "Turning raw data into decisions that matter.",
    "bio": (
        "I'm a data scientist based in Kimberley, South Africa, "
        "finishing an Honours degree at Sol Plaatje University. "
        "I build end-to-end machine learning systems — from exploratory analysis "
        "through production deployment — with a focus on computer vision, NLP, "
        "and predictive modelling. I'm currently open to data scientist, "
        "ML engineer, and research roles."
    ),
    "contact": {
        "email": "yourname@gmail.com",
        "phone": "+27 000 000 000",
        "location": "Kimberley, South Africa",
        "github": "https://github.com/",
        "linkedin": "https://www.linkedin.com/",
        "kaggle": "https://www.kaggle.com/",
    },
    
    "education": [
        {
            "degree": "Masters of Science In Computer & Information Science (Data Science)",
            "institution": "Sol Plaatje University",
            "period": "Jan 2026 – Present",
            "grade": "In progress",
            "highlights": ["Advanced Research", "Sound Analysis Systems", "Academic writing"],
        },
        {
            "degree": "Bachelor of Science Honours In Data Science",
            "institution": "Sol Plaatje University",
            "period": "Jan 2025 – Dec 2025",
            "grade": "76% average",
            "highlights": ["Advanced AI & deep learning research", "Big data analytics", "Research methodology"],
        },
        {
            "degree": "Bachelor of Science In Data Science",
            "institution": "Sol Plaatje University",
            "period": "Jan 2022 – Dec 2024",
            "grade": "81% average",
            "highlights": ["Machine learning specialisation", "Data engineering", "Statistics"],
        },
    ],
    "experience": [
        {
            "title": "Peer Mentor",
            "org": "Sol Plaatje University",
            "period": "Jan 2025 – Present",
            "points": [
                "Provide academic guidance to 50+ undergraduate students",
                "Contributed to a 15% improvement in retention rates",
                "Developed workshop materials and study resources",
            ],
        },
        {
            "title": "Academic Support Specialist",
            "org": "Sol Plaatje University",
            "period": "Jan 2025 – Present",
            "points": [
                "Delivered 100+ hours of tutoring in data science modules",
                "Mentored 20+ students through independent research",
            ],
        },
    ],
    "projects": [
        {
            "title": "Skin Disease Detection",
            "summary": "CNN-based classifier for dermatological conditions, achieving 94% accuracy.",
            "tags": ["Python", "TensorFlow", "CNN", "OpenCV"],
            "github": "#",
            "kaggle": "#",
            "status": "Completed",
        },
        {
            "title": "Monkeypox Detection & XAI",
            "summary": "Deep learning pipeline with Federated Learning and SHAP for clinical interpretability.",
            "tags": ["Federated Learning", "XAI", "SHAP", "CNN"],
            "github": "#",
            "kaggle": "#",
            "status": "Completed",
        },
    ],
    "skills": {
        "Programming": ["Python", "R", "SQL", "C++"],
        "Machine Learning": ["Scikit-learn", "XGBoost", "TensorFlow", "PyTorch"],
        "Databases": ["PostgreSQL", "MySQL", "MongoDB", "SQLite"],
    },
    "proficiency": [
        ("Python", 95),
        ("Machine Learning", 90),
        ("SQL", 85),
    ],
}

# ─────────────────────────────────────────────
# GLOBAL CSS
# ─────────────────────────────────────────────
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=DM+Serif+Display&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    color: #1a1a1a;
    overflow-x: hidden;
}

:root {
    --ink: #1a1a1a; --ink-2: #4a4a4a; --ink-3: #8a8a8a; --rule: #e4e4e4;
    --surface: #f8f7f5; --white: #ffffff; --accent: #1a3a5c;
    --accent-light: #eef2f7; --highlight: #c8a96e; --radius: 4px;
}

.block-container { padding: 0 !important; max-width: 100% !important; }
[data-testid="stHeader"] { background: rgba(0,0,0,0); }

.hero { background-color: var(--accent); padding: 72px 60px; position: relative; overflow: hidden; }
.hero-name { font-family: 'DM Serif Display', serif; font-size: 3.5rem; color: #fff; margin-bottom: 10px; }
.hero-tagline { font-size: 1.2rem; color: rgba(255,255,255,0.8); margin-bottom: 30px; }
.hero-link { 
    display: inline-block; padding: 8px 16px; border: 1px solid rgba(255,255,255,0.3); 
    border-radius: var(--radius); color: #fff !important; text-decoration: none; font-size: 13px; margin-right: 10px;
}

.stats-strip { display: flex; border-bottom: 1px solid var(--rule); background: #fff; }
.stat-cell { flex: 1; padding: 25px 60px; border-right: 1px solid var(--rule); }
.stat-num { font-family: 'DM Serif Display', serif; font-size: 1.8rem; color: var(--accent); }
.stat-label { font-size: 10px; text-transform: uppercase; letter-spacing: 1px; color: var(--ink-3); }

.body-wrapper { padding: 40px 60px; max-width: 1200px; margin: 0 auto; }
.section-title { font-family: 'DM Serif Display', serif; font-size: 1.8rem; margin-bottom: 25px; border-bottom: 1px solid var(--rule); padding-bottom: 10px; }
.card { background: #fff; border: 1px solid var(--rule); padding: 25px; border-radius: 8px; margin-bottom: 20px; transition: 0.3s; }
.card:hover { box-shadow: 0 10px 30px rgba(0,0,0,0.05); }

.tag { display: inline-block; padding: 3px 10px; background: var(--surface); border: 1px solid var(--rule); font-size: 11px; margin: 3px; border-radius: 3px; }
.badge-period { background: var(--accent-light); color: var(--accent); padding: 4px 10px; font-size: 11px; border-radius: 4px; }

/* Status Badges */
.badge-status-done { background: #e8f5e9; color: #2e7d32; padding: 3px 8px; font-size: 10px; border-radius: 3px; font-weight: 600; }
.badge-status-wip { background: #fff3e0; color: #ef6c00; padding: 3px 8px; font-size: 10px; border-radius: 3px; font-weight: 600; }

.prog-track { height: 4px; background: var(--rule); border-radius: 2px; margin-top: 5px; }
.prog-fill { height: 100%; background: var(--accent); border-radius: 2px; }
</style>
""",
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────
# COMPONENTS
# ─────────────────────────────────────────────
c = cv_data["contact"]
st.markdown(f"""
<div class="hero">
    <div style="color:var(--highlight); font-weight:600; letter-spacing:2px; font-size:12px;">PORTFOLIO</div>
    <div class="hero-name">{cv_data['name']}</div>
    <div class="hero-tagline">{cv_data['tagline']}</div>
    <div class="hero-links">
        <a href="mailto:{c['email']}" class="hero-link">✉ Email</a>
        <a href="{c['github']}" target="_blank" class="hero-link">⌥ GitHub</a>
        <a href="{c['linkedin']}" target="_blank" class="hero-link">↗ LinkedIn</a>
    </div>
</div>
<div class="stats-strip">
    <div class="stat-cell"><div class="stat-num">3+</div><div class="stat-label">Years Exp</div></div>
    <div class="stat-cell"><div class="stat-num">{len(cv_data['projects'])}</div><div class="stat-label">Projects</div></div>
    <div class="stat-cell"><div class="stat-num">81%</div><div class="stat-label">Avg Grade</div></div>
</div>
""", unsafe_allow_html=True)

tab_about, tab_resume, tab_projects, tab_skills, tab_contact = st.tabs(["About", "Résumé", "Projects", "Skills", "Contact"])

with tab_about:
    st.markdown('<div class="body-wrapper">', unsafe_allow_html=True)
    col1, col2 = st.columns([3, 2], gap="large")
    with col1:
        st.markdown(f"""<div class="section-title">Background</div><div class="card">{cv_data['bio']}</div>""", unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="section-title">Expertise</div>', unsafe_allow_html=True)
        for s, d in [("AI Systems", "End-to-end ML deployment"), ("Data Strategy", "Insight-driven decisions")]:
            st.markdown(f'<div class="card" style="padding:15px;"><b>{s}</b><br><small>{d}</small></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tab_resume:
    st.markdown('<div class="body-wrapper">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Education</div>', unsafe_allow_html=True)
    for edu in cv_data["education"]:
        st.markdown(f"""
        <div class="card">
            <div style="display:flex; justify-content:space-between;">
                <b>{edu['degree']}</b>
                <span class="badge-period">{edu['period']}</span>
            </div>
            <div style="color:var(--accent); font-size:13px; margin:5px 0;">{edu['institution']} • {edu['grade']}</div>
            <ul style="font-size:14px; color:var(--ink-2);">{ "".join(f"<li>{h}</li>" for h in edu['highlights']) }</ul>
        </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tab_projects:
    st.markdown('<div class="body-wrapper">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Selected Projects</div>', unsafe_allow_html=True)
    for p in cv_data["projects"]:
        status_cls = "badge-status-done" if p["status"] == "Completed" else "badge-status-wip"
        st.markdown(f"""
        <div class="card">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <h4 style="margin:0;">{p['title']}</h4>
                <span class="{status_cls}">{p['status']}</span>
            </div>
            <p style="font-size:14px; margin:10px 0;">{p['summary']}</p>
            <div>{"".join(f'<span class="tag">{t}</span>' for t in p['tags'])}</div>
            <div style="margin-top:15px;">
                <a href="{p['github']}" style="font-size:12px; color:var(--accent); text-decoration:none; margin-right:15px;">↗ GitHub</a>
                <a href="{p['kaggle']}" style="font-size:12px; color:var(--accent); text-decoration:none;">◈ Kaggle</a>
            </div>
        </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tab_skills:
    st.markdown('<div class="body-wrapper">', unsafe_allow_html=True)
    col_l, col_r = st.columns(2, gap="large")
    with col_l:
        st.markdown('<div class="section-title">Technical Toolkit</div>', unsafe_allow_html=True)
        for cat, items in cv_data["skills"].items():
            st.markdown(f"**{cat}**")
            st.markdown(f"<div>{''.join(f'<span class="tag">{i}</span>' for i in items)}</div><br>", unsafe_allow_html=True)
    with col_r:
        st.markdown('<div class="section-title">Proficiency</div>', unsafe_allow_html=True)
        for name, val in cv_data["proficiency"]:
            st.markdown(f"""
            <div style="margin-bottom:15px;">
                <div style="display:flex; justify-content:space-between; font-size:13px;"><span>{name}</span><span>{val}%</span></div>
                <div class="prog-track"><div class="prog-fill" style="width:{val}%"></div></div>
            </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tab_contact:
    st.markdown('<div class="body-wrapper">', unsafe_allow_html=True)
    c1, c2 = st.columns([2, 3], gap="large")
    with c1:
        st.markdown('<div class="section-title">Contact</div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="card">
            <p><small>EMAIL</small><br>{c['email']}</p>
            <p><small>LOCATION</small><br>{c['location']}</p>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="section-title">Message Me</div>', unsafe_allow_html=True)
        with st.form("contact", clear_on_submit=True):
            name = st.text_input("Name")
            email = st.text_input("Email")
            subj = st.selectbox("Subject", ["Job opportunity", "Collaboration", "Other"])
            msg = st.text_area("Message")
            if st.form_submit_button("Send"):
                if name and email and msg:
                    st.success("Message sent! I'll get back to you soon.")
                else:
                    st.error("Please fill in all fields.")
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown(f"""<div style="text-align:center; padding:40px; color:#8a8a8a; font-size:12px; border-top:1px solid #eee;">
© {datetime.now().year} {cv_data['name']} • Built with Streamlit</div>""", unsafe_allow_html=True)
