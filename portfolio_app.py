import streamlit as st
from datetime import datetime

# ---------------------------------------------
# PAGE CONFIG
# ---------------------------------------------
st.set_page_config(
    page_title="Portfolio | Data Scientist",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------
# SESSION STATE
# ---------------------------------------------
if "contact_submissions" not in st.session_state:
    st.session_state.contact_submissions = []

# ---------------------------------------------
# DATA
# ---------------------------------------------
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
        "email": "@gmail.com",
        "phone": "+27000",
        "location": "South Africa",
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
            "highlights": [
                "Advanced Research",
                "Sound Analysis Systems",
                "Academic writing",
            ],
        },
        {
            "degree": "Bachelor of Science Honours In Data Science",
            "institution": "Sol Plaatje University",
            "period": "January 2025 – December 2025",
            "grade": "76% average",
            "highlights": [
                "Advanced AI & deep learning research",
                "Big data analytics and distributed systems",
                "Research methodology and academic writing",
            ],
        },
        {
            "degree": "Bachelor of Science In Data Science",
            "institution": "Sol Plaatje University",
            "period": "January 2022 – December 2024",
            "grade": "81% average",
            "highlights": [
                "Machine learning specialisation",
                "Data engineering and database systems",
                "Statistics and probability theory",
            ],
        },
    ],
    "experience": [
        {
            "title": "Peer Mentor",
            "org": "Sol Plaatje University",
            "period": "Jan 2025 – Present",
            "points": [
                "Provide academic guidance and study support to 50+ undergraduate students",
                "Contributed to a 15% improvement in student module retention rates",
                "Developed workshop materials and interactive study resources",
            ],
        },
        {
            "title": "Academic Support Specialist",
            "org": "Sol Plaatje University",
            "period": "Jan 2025 – Present",
            "points": [
                "Delivered 100+ hours of tutoring across core data science modules",
                "Created interactive resources used by multiple cohorts",
                "Mentored 20+ students through independent research projects",
            ],
        },
        {
            "title": "Teaching Assistant",
            "org": "Homevale High School",
            "period": "Jan 2023 – Dec 2023",
            "points": [
                "Assisted in STEM curriculum development for Grades 10–12",
                "Tutored 30+ learners in computer science and mathematics",
                "Introduced digital learning tools to supplement classroom instruction",
            ],
        },
    ],
    "projects": [
        {
            "title": "Skin Disease Detection",
            "summary": "CNN-based classifier for dermatological conditions, achieving 94% accuracy on held-out test data.",
            "tags": ["Python", "TensorFlow", "CNN", "OpenCV", "Flask"],
            "github": "https://github.com/bbbbb/skin-disease",
            "kaggle": "https://www.kaggle.com/bbbb/skin-disease",
            "status": "Completed",
        },
        {
            "title": "Network Traffic Anomaly Detection",
            "summary": "Real-time intrusion detection system using unsupervised ML to flag suspicious network behaviour.",
            "tags": ["Python", "Scikit-learn", "Streamlit", "Cybersecurity"],
            "github": "https://github.com/bbbbb/network-traffic",
            "kaggle": "https://www.kaggle.com/bbbb/network-traffic",
            "status": "Active",
        },
        {
            "title": "Breast Cancer Classification",
            "summary": "Ensemble model achieving 97% accuracy with SHAP-based explainability for clinical interpretability.",
            "tags": ["Python", "XGBoost", "Feature Engineering", "SHAP"],
            "github": "https://github.com/bbbbb/breast-cancer",
            "kaggle": "https://www.kaggle.com/bbbb/breast-cancer",
            "status": "Completed",
        },
        {
            "title": "University Chatbot",
            "summary": "Transformer-based NLP chatbot answering student queries about courses, schedules, and campus services.",
            "tags": ["Python", "Transformers", "NLTK", "FastAPI", "Docker"],
            "github": "https://github.com/bbbbb/university-chatbot",
            "kaggle": "https://www.kaggle.com/bbbb/university-chatbot",
            "status": "In Progress",
        },
        {
            "title": "Monkeypox Detection Using Deep Learning & XAI",
            "summary": "Deep learning pipeline for monkeypox image classification, incorporating Federated learning to enable privacy-preserving training.",
            "tags": ["Python", "TensorFlow", "Federated Learning", "XAI", "SHAP", "CNN"],
            "github": "https://github.com/bbbbb/monkeypox-detection",
            "kaggle": "https://www.kaggle.com/bbbb/monkeypox-detection",
            "status": "Completed",
        },
    ],
    "skills": {
        "Programming": ["Python", "R", "SQL", "C++"],
        "Machine Learning": ["Scikit-learn", "XGBoost", "TensorFlow", "PyTorch"],
        "Data & Analytics": ["Pandas", "NumPy", "Spark", "Statistical Modelling"],
        "Visualisation": ["Tableau", "Power BI", "Plotly", "Seaborn"],
        "Infrastructure": ["Docker", "AWS", "Git / GitHub", "Linux", "CI/CD"],
        "Databases": ["PostgreSQL", "MySQL", "MongoDB", "SQLite"],
    },
    "proficiency": [
        ("Python", 95),
        ("Machine Learning", 90),
        ("Data Visualisation", 88),
        ("SQL", 85),
        ("Deep Learning", 82),
    ],
}

# ---------------------------------------------
# GLOBAL CSS
# ---------------------------------------------
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,300&family=DM+Serif+Display:ital@0;1&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    font-size: 16px;
    color: #1a1a1a;
}

:root {
    --ink: #1a1a1a; --ink-2: #4a4a4a; --ink-3: #8a8a8a; --rule: #e4e4e4;
    --surface: #f8f7f5; --white: #ffffff; --accent: #1a3a5c;
    --accent-light: #eef2f7; --accent-mid: #7a9fbf; --highlight: #c8a96e;
    --radius: 4px; --radius-lg: 8px;
}

.block-container { padding: 0 !important; max-width: 100% !important; }
#MainMenu, footer, header { visibility: hidden; }

.hero { background-color: var(--accent); padding: 72px 60px 64px; position: relative; overflow: hidden; }
.hero-kicker { font-size: 12px; font-weight: 600; letter-spacing: 0.16em; text-transform: uppercase; color: var(--highlight); margin-bottom: 16px; }
.hero-name { font-family: 'DM Serif Display', serif; font-size: clamp(2.4rem, 5vw, 3.8rem); color: #ffffff; line-height: 1.1; margin-bottom: 20px; }
.hero-tagline { font-size: 1.15rem; font-weight: 300; color: rgba(255,255,255,0.75); margin-bottom: 36px; max-width: 520px; line-height: 1.6; }
.hero-link { display: inline-flex; align-items: center; gap: 6px; padding: 9px 18px; border: 1px solid rgba(255,255,255,0.25); border-radius: var(--radius); color: white !important; text-decoration: none !important; font-size: 13px; transition: 0.2s; }
.hero-link:hover { background: rgba(255,255,255,0.1); border-color: white; }

.stats-strip { display: grid; grid-template-columns: repeat(4, 1fr); border-top: 1px solid var(--rule); border-bottom: 1px solid var(--rule); background: var(--white); }
.stat-cell { padding: 28px 32px; border-right: 1px solid var(--rule); }
.stat-cell:last-child { border-right: none; }
.stat-num { font-family: 'DM Serif Display', serif; font-size: 2rem; color: var(--accent); }
.stat-label { font-size: 11px; font-weight: 600; text-transform: uppercase; color: var(--ink-3); }

.body-wrapper { padding: 52px 60px; max-width: 1200px; margin: 0 auto; }
.section-title { font-family: 'DM Serif Display', serif; font-size: 1.75rem; margin-bottom: 32px; padding-bottom: 16px; border-bottom: 1px solid var(--rule); }

.card { background: var(--white); border: 1px solid var(--rule); border-radius: var(--radius-lg); padding: 28px 30px; margin-bottom: 20px; transition: 0.2s; }
.card:hover { box-shadow: 0 4px 20px rgba(26,58,92,0.08); }
.card-title { font-family: 'DM Serif Display', serif; font-size: 1.2rem; color: var(--ink); }
.badge-period { padding: 4px 12px; background: var(--accent-light); color: var(--accent); border-radius: 2px; font-size: 12px; }

.edu-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-bottom: 32px; }
.tags-row { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 14px; }
.tag { padding: 4px 11px; background: var(--surface); border: 1px solid var(--rule); font-size: 12px; border-radius: 2px; }

.prog-track { height: 3px; background: var(--rule); margin-top: 6px; }
.prog-fill { height: 100%; background: var(--accent); }

@media (max-width: 900px) {
    .edu-grid, .stats-strip { grid-template-columns: 1fr; }
    .body-wrapper { padding: 32px 20px; }
}
</style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------
# HERO
# ---------------------------------------------
c = cv_data["contact"]
st.markdown(
    f"""
<div class="hero">
    <div class="hero-kicker">Data Scientist · Kimberley, South Africa</div>
    <div class="hero-name">{cv_data['name']}</div>
    <div class="hero-tagline">{cv_data['tagline']}</div>
    <div class="hero-links">
        <a href="mailto:{c['email']}" class="hero-link">✉ Email</a>
        <a href="{c['github']}" target="_blank" class="hero-link">⌥ GitHub</a>
        <a href="{c['kaggle']}" target="_blank" class="hero-link">◈ Kaggle</a>
        <a href="{c['linkedin']}" target="_blank" class="hero-link">↗ LinkedIn</a>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------
# STATS STRIP
# ---------------------------------------------
st.markdown(
    """
<div class="stats-strip">
    <div class="stat-cell"><div class="stat-num">3+</div><div class="stat-label">Years experience</div></div>
    <div class="stat-cell"><div class="stat-num">15+</div><div class="stat-label">Projects delivered</div></div>
    <div class="stat-cell"><div class="stat-num">10+</div><div class="stat-label">Technologies</div></div>
    <div class="stat-cell"><div class="stat-num">81%</div><div class="stat-label">Degree average</div></div>
</div>
""",
    unsafe_allow_html=True,
)

tab_about, tab_resume, tab_projects, tab_skills, tab_contact = st.tabs(
    ["About", "Résumé", "Projects", "Skills", "Contact"]
)

with tab_about:
    st.markdown('<div class="body-wrapper">', unsafe_allow_html=True)
    col_bio, col_offers = st.columns([3, 2], gap="large")
    with col_bio:
        st.markdown(f"""
            <div class="section-title">About me</div>
            <div class="card"><p>{cv_data['bio']}</p></div>
        """, unsafe_allow_html=True)
    with col_offers:
        st.markdown('<div class="section-title">Core strengths</div>', unsafe_allow_html=True)
        for title, desc in [("AI Systems", "Custom models."), ("Insight", "Data decisions.")]:
            st.markdown(f'<div class="card"><b>{title}</b><br>{desc}</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with tab_resume:
    st.markdown('<div class="body-wrapper">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Education</div>', unsafe_allow_html=True)
    edu_html = '<div class="edu-grid">'
    for edu in cv_data["education"]:
        h_html = "".join(f"<li>{h}</li>" for h in edu["highlights"])
        edu_html += f"""
        <div class="card">
            <div class="card-title">{edu['degree']}</div>
            <div class="badge-period">{edu['period']}</div>
            <ul>{h_html}</ul>
        </div>"""
    st.markdown(edu_html + "</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with tab_projects:
    st.markdown('<div class="body-wrapper">', unsafe_allow_html=True)
    for proj in cv_data["projects"]:
        st.markdown(f"""
        <div class="card">
            <div class="card-title">{proj['title']}</div>
            <p>{proj['summary']}</p>
            <div class="tags-row">{''.join(f'<span class="tag">{t}</span>' for t in proj['tags'])}</div>
        </div>""", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with tab_skills:
    st.markdown('<div class="body-wrapper">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        for cat, items in cv_data["skills"].items():
            st.markdown(f"**{cat}**: {', '.join(items)}")
    with col2:
        for skill, level in cv_data["proficiency"]:
            st.markdown(f"{skill} ({level}%)")
            st.progress(level/100)
    st.markdown("</div>", unsafe_allow_html=True)

with tab_contact:
    st.markdown('<div class="body-wrapper">', unsafe_allow_html=True)
    with st.form("contact"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        msg = st.text_area("Message")
        if st.form_submit_button("Send"):
            st.success("Message sent!")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------
# FOOTER
# ---------------------------------------------
st.markdown(
    f"""
<div style="border-top: 1px solid #e4e4e4; padding: 32px 60px; display: flex; justify-content: space-between; background: #f8f7f5;">
    <div>{cv_data['name']} | {cv_data['title']}</div>
    <div style="font-size: 12px; color: #8a8a8a;">© {datetime.now().year}</div>
</div>
""",
    unsafe_allow_html=True,
)
