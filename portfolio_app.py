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
        "phone": "+27 000 000 0000",
        "location": "Kimberley, South Africa",
        "github": "https://github.com/yourusername",
        "linkedin": "https://www.linkedin.com/in/yourprofile",
        "kaggle": "https://www.kaggle.com/yourusername",
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
            "github": "https://github.com/yourusername/skin-disease",
            "kaggle": "https://www.kaggle.com/yourusername/skin-disease",
            "status": "Completed",
        },
        {
            "title": "Network Traffic Anomaly Detection",
            "summary": "Real-time intrusion detection system using unsupervised ML to flag suspicious network behaviour.",
            "tags": ["Python", "Scikit-learn", "Streamlit", "Cybersecurity"],
            "github": "https://github.com/yourusername/network-traffic",
            "kaggle": "https://www.kaggle.com/yourusername/network-traffic",
            "status": "Active",
        },
        {
            "title": "Breast Cancer Classification",
            "summary": "Ensemble model achieving 97% accuracy with SHAP-based explainability for clinical interpretability.",
            "tags": ["Python", "XGBoost", "Feature Engineering", "SHAP"],
            "github": "https://github.com/yourusername/breast-cancer",
            "kaggle": "https://www.kaggle.com/yourusername/breast-cancer",
            "status": "Completed",
        },
        {
            "title": "University Chatbot",
            "summary": "Transformer-based NLP chatbot answering student queries about courses, schedules, and campus services.",
            "tags": ["Python", "Transformers", "NLTK", "FastAPI", "Docker"],
            "github": "https://github.com/yourusername/university-chatbot",
            "kaggle": "https://www.kaggle.com/yourusername/university-chatbot",
            "status": "In Progress",
        },
        {
            "title": "Monkeypox Detection Using Deep Learning & Explainable AI with Federated Learning",
            "summary": "Deep learning pipeline for monkeypox image classification, incorporating Explainable AI (XAI) techniques and federated learning to enable privacy-preserving model training across distributed medical datasets.",
            "tags": ["Python", "TensorFlow", "Federated Learning", "XAI", "SHAP", "CNN"],
            "github": "https://github.com/yourusername/monkeypox-detection",
            "kaggle": "https://www.kaggle.com/yourusername/monkeypox-detection",
            "status": "Completed",
        },
        {
            "title": "Cryptographic Analysis System",
            "summary": "System for analysing and evaluating cryptographic algorithms, supporting cipher identification, key analysis, and vulnerability assessment across classical and modern encryption schemes.",
            "tags": ["Python", "Cryptography", "Security", "Algorithm Analysis"],
            "github": "https://github.com/yourusername/crypto-analysis",
            "kaggle": "https://www.kaggle.com/yourusername/crypto-analysis",
            "status": "Completed",
        },
        {
            "title": "Content-Based Filtering Recommender System",
            "summary": "Recommender system using content-based filtering to deliver personalised suggestions by analysing item features and user preference profiles with TF-IDF and cosine similarity.",
            "tags": ["Python", "Scikit-learn", "NLP", "TF-IDF", "Recommender Systems"],
            "github": "https://github.com/yourusername/recommender-system",
            "kaggle": "https://www.kaggle.com/yourusername/recommender-system",
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

# ─────────────────────────────────────────────
# GLOBAL CSS
# ─────────────────────────────────────────────
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,300&family=DM+Serif+Display:ital@0;1&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif !important;
    font-size: 16px;
}

/* ── Force Streamlit background & text ── */
[data-testid="stAppViewContainer"],
[data-testid="stAppViewContainer"] > .main {
    background-color: #e8eef2 !important;  /* Soft blue-gray */
}

[data-testid="stAppViewContainer"] section.main > div {
    background-color: #e8eef2 !important;
}

/* Force all markdown text to be visible */
[data-testid="stMarkdownContainer"],
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] div,
[data-testid="stMarkdownContainer"] span,
[data-testid="stMarkdownContainer"] li,
[data-testid="stMarkdownContainer"] a {
    font-family: 'DM Sans', sans-serif !important;
}

/* ── Layout ── */
.block-container { padding: 0 !important; max-width: 100% !important; }
#MainMenu, footer, header { visibility: hidden; }

/* ── Hero ── */
.hero {
    background-color: #1a3a5c;  /* Navy - keeps contrast */
    padding: 72px 60px 64px;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 320px; height: 320px;
    border-radius: 50%;
    border: 1px solid rgba(255,255,255,0.06);
}
.hero::after {
    content: '';
    position: absolute;
    bottom: -40px; left: 40px;
    width: 180px; height: 180px;
    border-radius: 50%;
    border: 1px solid rgba(255,255,255,0.04);
}
.hero-kicker {
    font-size: 12px !important;
    font-weight: 600 !important;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: #c8a96e !important;  /* Warm gold */
    margin-bottom: 16px;
}
.hero-name {
    font-family: 'DM Serif Display', serif !important;
    font-size: clamp(2.4rem, 5vw, 3.8rem) !important;
    font-weight: 400 !important;
    color: #ffffff !important;
    line-height: 1.1;
    margin-bottom: 20px;
}
.hero-tagline {
    font-size: 1.15rem !important;
    font-weight: 300 !important;
    color: rgba(255,255,255,0.75) !important;
    margin-bottom: 36px;
    max-width: 520px;
    line-height: 1.6;
}
.hero-links { display: flex; gap: 12px; flex-wrap: wrap; }
.hero-link {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 9px 18px;
    border: 1px solid rgba(255,255,255,0.25);
    border-radius: 4px;
    color: rgba(255,255,255,0.9) !important;
    text-decoration: none !important;
    font-size: 13px !important;
    font-weight: 500;
    letter-spacing: 0.02em;
    transition: border-color 0.2s, background-color 0.2s;
}
.hero-link:hover {
    border-color: rgba(255,255,255,0.6);
    background-color: rgba(255,255,255,0.07);
    color: #ffffff !important;
}

/* ── Stats strip ── */
.stats-strip {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    border-top: 1px solid #c4d4dc;  /* Blue-gray border */
    border-bottom: 1px solid #c4d4dc;
    background: #f0f5f8;  /* Light blue-white */
}
.stat-cell {
    padding: 28px 32px;
    border-right: 1px solid #c4d4dc;
}
.stat-cell:last-child { border-right: none; }
.stat-num {
    font-family: 'DM Serif Display', serif !important;
    font-size: 2rem !important;
    color: #1a3a5c !important;  /* Navy */
    line-height: 1;
    margin-bottom: 4px;
}
.stat-label {
    font-size: 11px !important;
    font-weight: 600 !important;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #5a6a7a !important;  /* Blue-gray */
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    gap: 0;
    border-bottom: 1px solid #c4d4dc;  /* Blue-gray border */
    background: #f0f5f8;  /* Light blue-white */
    padding: 0 60px;
}
.stTabs [data-baseweb="tab"] {
    padding: 14px 22px;
    font-size: 13px !important;
    font-weight: 500;
    letter-spacing: 0.04em;
    color: #5a6a7a !important;  /* Blue-gray */
    border-bottom: 2px solid transparent;
    transition: color 0.15s, border-color 0.15s;
    background: transparent !important;
}
.stTabs [aria-selected="true"] {
    color: #1a3a5c !important;  /* Navy */
    border-bottom: 2px solid #1a3a5c !important;
}

/* ── Card backgrounds (for all sections) ── */
/* This will apply to all your inline card divs */

/* ── Form elements ── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    border-radius: 4px;
    border: 1px solid #c4d4dc;  /* Blue-gray border */
    font-family: 'DM Sans', sans-serif !important;
    font-size: 14px;
    padding: 10px 14px;
    background: #f0f5f8;  /* Light blue-white */
    color: #1a2a3a !important;  /* Dark blue-black */
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #7a9fbf;
    box-shadow: 0 0 0 3px rgba(26,58,92,0.07);
    background: #f0f5f8;
}
.stTextInput label, .stTextArea label, .stSelectbox label {
    color: #1a2a3a !important;  /* Dark blue-black */
    font-size: 14px !important;
    font-weight: 500 !important;
}
.stButton > button {
    background: #1a3a5c !important;  /* Navy */
    color: white !important;
    border: none !important;
    border-radius: 4px;
    padding: 12px 28px;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 14px;
    font-weight: 500;
    letter-spacing: 0.03em;
    width: 100%;
    transition: background-color 0.15s;
}
.stButton > button:hover { background: #152e4a !important; }
.stSelectbox > div > div {
    border-radius: 4px;
    border: 1px solid #c4d4dc !important;  /* Blue-gray border */
    background: #f0f5f8;  /* Light blue-white */
    font-size: 14px;
    color: #1a2a3a !important;  /* Dark blue-black */
}
</style>

""",
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────
def kicker(text):
    return f'<div style="font-size:11px;font-weight:600;letter-spacing:0.16em;text-transform:uppercase;color:#c8a96e;margin-bottom:8px;">{text}</div>'

def section_title(text):
    return f'<div style="font-family:\'DM Serif Display\',serif;font-size:1.75rem;font-weight:400;color:#1a1a1a;margin-bottom:32px;padding-bottom:16px;border-bottom:1px solid #e4e4e4;">{text}</div>'

def badge_period(text):
    return f'<span style="display:inline-block;padding:4px 12px;background:#eef2f7;color:#1a3a5c;border-radius:2px;font-size:12px;font-weight:500;white-space:nowrap;">{text}</span>'

def tag(text):
    return f'<span style="display:inline-block;padding:4px 11px;background:#f8f7f5;color:#4a4a4a;border:1px solid #e4e4e4;border-radius:2px;font-size:12px;font-weight:500;">{text}</span>'

# ─────────────────────────────────────────────
# HERO
# ─────────────────────────────────────────────
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

# ─────────────────────────────────────────────
# STATS STRIP
# ─────────────────────────────────────────────
st.markdown(
    """
<div class="stats-strip">
    <div class="stat-cell">
        <div class="stat-num">3+</div>
        <div class="stat-label">Years experience</div>
    </div>
    <div class="stat-cell">
        <div class="stat-num">15+</div>
        <div class="stat-label">Projects delivered</div>
    </div>
    <div class="stat-cell">
        <div class="stat-num">10+</div>
        <div class="stat-label">Technologies</div>
    </div>
    <div class="stat-cell">
        <div class="stat-num">81%</div>
        <div class="stat-label">Degree average</div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────
# TABS
# ─────────────────────────────────────────────
tab_about, tab_resume, tab_projects, tab_skills, tab_contact = st.tabs(
    ["About", "Résumé", "Projects", "Skills", "Contact"]
)

# ──────────────────────────
# TAB 1 — ABOUT
# ──────────────────────────
with tab_about:
    st.markdown('<div style="padding:52px 60px;max-width:1200px;margin:0 auto;">', unsafe_allow_html=True)

    col_bio, col_offers = st.columns([3, 2], gap="large")

    with col_bio:
        tags_html = "".join(tag(t) for t in ["Open to work", "Data Science", "ML Engineering", "Research"])
        st.markdown(
            kicker("Background") + section_title("About me") +
            f"""
            <div style="background:#ffffff;border:1px solid #e4e4e4;border-radius:8px;padding:28px 30px;margin-bottom:20px;">
                <p style="font-size:15px;color:#4a4a4a;line-height:1.65;margin:0;">{cv_data['bio']}</p>
                <div style="display:flex;flex-wrap:wrap;gap:6px;margin-top:20px;">{tags_html}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_offers:
        st.markdown(kicker("What I bring") + section_title("Core strengths"), unsafe_allow_html=True)

        strengths = [
            ("AI & ML Systems", "Custom models from prototyping through production deployment."),
            ("Data Insight", "Translating messy datasets into clear, actionable decisions."),
            ("End-to-End Delivery", "Full project lifecycle ownership, solo or in a team."),
            ("Communication", "Making technical findings accessible to non-technical audiences."),
        ]
        for title, desc in strengths:
            st.markdown(
                f"""
                <div style="background:#ffffff;border:1px solid #e4e4e4;border-radius:8px;padding:18px 22px;margin-bottom:12px;">
                    <div style="font-weight:600;font-size:15px;color:#1a1a1a;margin-bottom:4px;">{title}</div>
                    <div style="font-size:14px;color:#4a4a4a;line-height:1.55;">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("</div>", unsafe_allow_html=True)


# ──────────────────────────
# TAB 2 — RÉSUMÉ
# ──────────────────────────
with tab_resume:
    st.markdown('<div style="padding:52px 60px;max-width:1200px;margin:0 auto;">', unsafe_allow_html=True)

    st.markdown(kicker("Academic history") + section_title("Education"), unsafe_allow_html=True)

    edu_cols = st.columns(2, gap="medium")
    for col, edu in zip(edu_cols, cv_data["education"]):
        with col:
            highlights_html = "".join(f"<li style='margin-bottom:6px;color:#4a4a4a;'>{h}</li>" for h in edu["highlights"])
            st.markdown(
                f"""
                <div style="background:#ffffff;border:1px solid #e4e4e4;border-radius:8px;padding:28px 30px;margin-bottom:20px;">
                    <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:8px;margin-bottom:10px;">
                        <div>
                            <div style="font-family:'DM Serif Display',serif;font-size:1.1rem;color:#1a1a1a;line-height:1.3;">{edu['degree']}</div>
                            <div style="font-size:14px;color:#4a4a4a;margin-top:4px;">{edu['institution']}</div>
                        </div>
                        {badge_period(edu['period'])}
                    </div>
                    <div style="font-size:13px;font-weight:600;color:#1a3a5c;margin:10px 0 4px;">{edu['grade']}</div>
                    <ul style="padding-left:20px;margin-top:8px;font-size:14px;line-height:1.65;">{highlights_html}</ul>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown(
        f'<div style="margin-top:24px;">{kicker("Work history")}{section_title("Experience")}</div>',
        unsafe_allow_html=True,
    )

    for exp in cv_data["experience"]:
        points_html = "".join(f"<li style='margin-bottom:6px;color:#4a4a4a;'>{p}</li>" for p in exp["points"])
        st.markdown(
            f"""
            <div style="background:#ffffff;border:1px solid #e4e4e4;border-radius:8px;padding:28px 30px;margin-bottom:20px;">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:8px;margin-bottom:10px;">
                    <div>
                        <div style="font-family:'DM Serif Display',serif;font-size:1.2rem;color:#1a1a1a;">{exp['title']}</div>
                        <div style="font-size:14px;color:#4a4a4a;margin-top:4px;">{exp['org']}</div>
                    </div>
                    {badge_period(exp['period'])}
                </div>
                <ul style="padding-left:20px;margin-top:8px;font-size:14px;line-height:1.65;">{points_html}</ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)


# ──────────────────────────
# TAB 3 — PROJECTS
# ──────────────────────────
with tab_projects:
    st.markdown('<div style="padding:52px 60px;max-width:1200px;margin:0 auto;">', unsafe_allow_html=True)

    st.markdown(kicker("Selected work") + section_title("Projects"), unsafe_allow_html=True)

    status_styles = {
        "Completed":   "background:#edf7f1;color:#1a7a42;",
        "Active":      "background:#fef9ee;color:#9a6b00;",
        "In Progress": "background:#eef2f7;color:#1a3a5c;",
    }

    for proj in cv_data["projects"]:
        tags_html = "".join(tag(t) for t in proj["tags"])
        badge_style = status_styles.get(proj["status"], "background:#eef2f7;color:#1a3a5c;")
        st.markdown(
            f"""
            <div style="background:#ffffff;border:1px solid #e4e4e4;border-radius:8px;padding:28px 30px;margin-bottom:20px;">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:8px;margin-bottom:8px;">
                    <div style="font-family:'DM Serif Display',serif;font-size:1.2rem;color:#1a1a1a;">{proj['title']}</div>
                    <span style="display:inline-block;padding:3px 10px;{badge_style}border-radius:2px;font-size:11px;font-weight:600;letter-spacing:0.04em;text-transform:uppercase;">{proj['status']}</span>
                </div>
                <div style="font-size:15px;color:#4a4a4a;line-height:1.65;margin-top:8px;">{proj['summary']}</div>
                <div style="display:flex;flex-wrap:wrap;gap:6px;margin-top:14px;">{tags_html}</div>
                <div style="display:flex;gap:8px;margin-top:16px;flex-wrap:wrap;">
                    <a href="{proj['github']}" target="_blank" style="display:inline-flex;align-items:center;gap:5px;padding:7px 14px;border:1px solid #e4e4e4;border-radius:4px;color:#4a4a4a;text-decoration:none;font-size:12px;font-weight:500;">↗ View code</a>
                    <a href="{proj['kaggle']}" target="_blank" style="display:inline-flex;align-items:center;gap:5px;padding:7px 14px;border:1px solid #e4e4e4;border-radius:4px;color:#4a4a4a;text-decoration:none;font-size:12px;font-weight:500;">◈ Kaggle notebook</a>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)


# ──────────────────────────
# TAB 4 — SKILLS
# ──────────────────────────
with tab_skills:
    st.markdown('<div style="padding:52px 60px;max-width:1200px;margin:0 auto;">', unsafe_allow_html=True)

    col_cats, col_prof = st.columns([3, 2], gap="large")

    with col_cats:
        st.markdown(kicker("Technical toolkit") + section_title("Skills by category"), unsafe_allow_html=True)

        for category, items in cv_data["skills"].items():
            tags_html = "".join(tag(item) for item in items)
            st.markdown(
                f"""
                <div style="margin-bottom:28px;">
                    <div style="font-size:11px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:#8a8a8a;margin-bottom:10px;padding-bottom:6px;border-bottom:1px solid #e4e4e4;">{category}</div>
                    <div style="display:flex;flex-wrap:wrap;gap:6px;">{tags_html}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    with col_prof:
        st.markdown(kicker("Self-assessed") + section_title("Proficiency"), unsafe_allow_html=True)

        for skill, level in cv_data["proficiency"]:
            st.markdown(
                f"""
                <div style="margin-bottom:18px;">
                    <div style="display:flex;justify-content:space-between;font-size:14px;font-weight:500;color:#1a1a1a;margin-bottom:6px;">
                        <span>{skill}</span>
                        <span style="color:#8a8a8a;font-weight:400;">{level}%</span>
                    </div>
                    <div style="height:3px;background:#e4e4e4;border-radius:2px;overflow:hidden;">
                        <div style="height:100%;width:{level}%;background:#1a3a5c;border-radius:2px;"></div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("</div>", unsafe_allow_html=True)


# ──────────────────────────
# TAB 5 — CONTACT
# ──────────────────────────
with tab_contact:
    st.markdown('<div style="padding:52px 60px;max-width:1200px;margin:0 auto;">', unsafe_allow_html=True)

    col_info, col_form = st.columns([2, 3], gap="large")

    with col_info:
        st.markdown(kicker("Get in touch") + section_title("Contact"), unsafe_allow_html=True)

        contact_data = cv_data["contact"]
        contact_items = [
            ("✉",  "Email",    f'<a href="mailto:{contact_data["email"]}" style="color:#1a3a5c;text-decoration:none;">{contact_data["email"]}</a>'),
            ("📱", "Phone",    contact_data["phone"]),
            ("◎",  "Location", contact_data["location"]),
            ("⌥",  "GitHub",   f'<a href="{contact_data["github"]}" target="_blank" style="color:#1a3a5c;text-decoration:none;">{contact_data["github"].replace("https://", "")}</a>'),
            ("↗",  "LinkedIn", f'<a href="{contact_data["linkedin"]}" target="_blank" style="color:#1a3a5c;text-decoration:none;">{contact_data["linkedin"].replace("https://", "").replace("www.", "")}</a>'),
        ]

        # Opening card wrapper
        st.markdown(
            '<div style="background:#ffffff;border:1px solid #e4e4e4;border-radius:8px;padding:8px 24px;">',
            unsafe_allow_html=True,
        )

        # One st.markdown() call per item to avoid Streamlit's code-block fallback
        for i, (icon, label, val) in enumerate(contact_items):
            border = "border-bottom:1px solid #e4e4e4;" if i < len(contact_items) - 1 else ""
            st.markdown(
                f"""
                <div style="display:flex;align-items:flex-start;gap:14px;padding:16px 0;{border}">
                    <div style="width:36px;height:36px;border-radius:4px;background:#eef2f7;
                                display:flex;align-items:center;justify-content:center;
                                flex-shrink:0;font-size:16px;line-height:1;">
                        {icon}
                    </div>
                    <div>
                        <div style="font-size:11px;font-weight:600;letter-spacing:0.08em;
                                    text-transform:uppercase;color:#8a8a8a;margin-bottom:2px;">
                            {label}
                        </div>
                        <div style="font-size:15px;color:#1a1a1a;">{val}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # Closing card wrapper
        st.markdown("</div>", unsafe_allow_html=True)

    with col_form:
        st.markdown(kicker("Send a message") + section_title("Say hello"), unsafe_allow_html=True)

        with st.form("contact_form", clear_on_submit=True):
            col_a, col_b = st.columns(2)
            with col_a:
                name = st.text_input("Name", placeholder="Your name")
            with col_b:
                email = st.text_input("Email", placeholder="you@example.com")

            subject = st.selectbox(
                "Subject",
                ["", "Job opportunity", "Project inquiry", "Collaboration", "Question", "Other"],
            )
            message = st.text_area("Message", height=140, placeholder="Your message…")
            submitted = st.form_submit_button("Send message")

            if submitted:
                if name and email and subject and message:
                    st.session_state.contact_submissions.append({
                        "name": name,
                        "email": email,
                        "subject": subject,
                        "message": message,
                        "timestamp": datetime.now().isoformat(),
                    })
                    st.success(f"Message received — thank you, {name}. I'll be in touch soon.")
                else:
                    st.warning("Please complete all fields before sending.")

    st.markdown("</div>", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────
st.markdown(
    f"""
<div style="border-top:1px solid #e4e4e4;padding:32px 60px;display:flex;justify-content:space-between;
            align-items:center;flex-wrap:wrap;gap:12px;background:#f8f7f5;">
    <div style="font-family:'DM Serif Display',serif;font-size:1.1rem;color:#1a1a1a;">
        {cv_data['name']}
        <span style="font-family:'DM Sans',sans-serif;font-size:0.8rem;font-weight:400;
                     color:#8a8a8a;margin-left:10px;">{cv_data['title']}</span>
    </div>
    <div style="font-size:12px;color:#8a8a8a;">
        © {datetime.now().year} · Kimberley, South Africa
    </div>
</div>
""",
    unsafe_allow_html=True,
)
