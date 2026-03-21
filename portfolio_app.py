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
    "name": "Bonolo Angela Rentsi",
    "initials": "BAR",
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
        "email": "bbbbbb@gmail.com",
        "phone": "+27 888888888888",
        "location": "Kimberley, South Africa",
        "github": "https://github.com/bbbbb",
        "linkedin": "https://linkedin.com/in/bbbb",
        "kaggle": "https://www.kaggle.com/bbbb",
    },
    "education": [
        {
            "degree": "BSc Honours — Computer Sciences",
            "institution": "Sol Plaatje University",
            "period": "Jan 2025 – Present",
            "grade": "78% average",
            "highlights": [
                "Advanced AI & deep learning research",
                "Big data analytics and distributed systems",
                "Research methodology and academic writing",
            ],
        },
        {
            "degree": "BSc — Computer Science / Data Science",
            "institution": "Sol Plaatje University",
            "period": "Jan 2022 – Dec 2024",
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
            "title": "Monkeypox Detection Using Deep Learning & Explainable AI with Federated Learning",
            "summary": "Deep learning pipeline for monkeypox image classification, incorporating Explainable AI (XAI) techniques and federated learning to enable privacy-preserving model training across distributed medical datasets.",
            "tags": ["Python", "TensorFlow", "Federated Learning", "XAI", "SHAP", "CNN"],
            "github": "https://github.com/bbbbb/monkeypox-detection",
            "kaggle": "https://www.kaggle.com/bbbb/monkeypox-detection",
            "status": "Completed",
        },
        {
            "title": "Cryptographic Analysis System",
            "summary": "System for analysing and evaluating cryptographic algorithms, supporting cipher identification, key analysis, and vulnerability assessment across classical and modern encryption schemes.",
            "tags": ["Python", "Cryptography", "Security", "Algorithm Analysis"],
            "github": "https://github.com/bbbbb/crypto-analysis",
            "kaggle": "https://www.kaggle.com/bbbb/crypto-analysis",
            "status": "Completed",
        },
        {
            "title": "Content-Based Filtering Recommender System",
            "summary": "Recommender system using content-based filtering to deliver personalised suggestions by analysing item features and user preference profiles with TF-IDF and cosine similarity.",
            "tags": ["Python", "Scikit-learn", "NLP", "TF-IDF", "Recommender Systems"],
            "github": "https://github.com/bbbbb/recommender-system",
            "kaggle": "https://www.kaggle.com/bbbb/recommender-system",
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
# GLOBAL CSS — refined editorial aesthetic
# ─────────────────────────────────────────────
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,300&family=DM+Serif+Display:ital@0;1&display=swap');

*, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    font-size: 16px;
    color: #1a1a1a;
}

:root {
    --ink: #1a1a1a;
    --ink-2: #4a4a4a;
    --ink-3: #8a8a8a;
    --rule: #e4e4e4;
    --surface: #f8f7f5;
    --white: #ffffff;
    --accent: #1a3a5c;
    --accent-light: #eef2f7;
    --accent-mid: #7a9fbf;
    --highlight: #c8a96e;
    --radius: 4px;
    --radius-lg: 8px;
}

/* ── Layout ── */
.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

#MainMenu, footer, header { visibility: hidden; }

/* ── Hero ── */
.hero {
    background-color: var(--accent);
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
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: var(--highlight);
    margin-bottom: 16px;
}

.hero-name {
    font-family: 'DM Serif Display', serif;
    font-size: clamp(2.4rem, 5vw, 3.8rem);
    font-weight: 400;
    color: #ffffff;
    line-height: 1.1;
    margin-bottom: 20px;
    letter-spacing: -0.01em;
}

.hero-tagline {
    font-size: 1.15rem;
    font-weight: 300;
    color: rgba(255,255,255,0.75);
    margin-bottom: 36px;
    max-width: 520px;
    line-height: 1.6;
}

.hero-links {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
}

.hero-link {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 9px 18px;
    border: 1px solid rgba(255,255,255,0.25);
    border-radius: var(--radius);
    color: rgba(255,255,255,0.9) !important;
    text-decoration: none !important;
    font-size: 13px;
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
    border-top: 1px solid var(--rule);
    border-bottom: 1px solid var(--rule);
    background: var(--white);
}

.stat-cell {
    padding: 28px 32px;
    border-right: 1px solid var(--rule);
}

.stat-cell:last-child { border-right: none; }

.stat-num {
    font-family: 'DM Serif Display', serif;
    font-size: 2rem;
    color: var(--accent);
    line-height: 1;
    margin-bottom: 4px;
}

.stat-label {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--ink-3);
}

/* ── Body layout ── */
.body-wrapper {
    padding: 52px 60px;
    max-width: 1200px;
    margin: 0 auto;
}

/* ── Section headings ── */
.section-kicker {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: var(--highlight);
    margin-bottom: 8px;
}

.section-title {
    font-family: 'DM Serif Display', serif;
    font-size: 1.75rem;
    font-weight: 400;
    color: var(--ink);
    margin-bottom: 32px;
    padding-bottom: 16px;
    border-bottom: 1px solid var(--rule);
}

/* ── Cards ── */
.card {
    background: var(--white);
    border: 1px solid var(--rule);
    border-radius: var(--radius-lg);
    padding: 28px 30px;
    margin-bottom: 20px;
    transition: box-shadow 0.2s;
}

.card:hover {
    box-shadow: 0 4px 20px rgba(26,58,92,0.08);
}

.card-meta {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 10px;
}

.card-title {
    font-family: 'DM Serif Display', serif;
    font-size: 1.2rem;
    font-weight: 400;
    color: var(--ink);
    margin: 0;
}

.card-sub {
    font-size: 0.875rem;
    color: var(--ink-2);
    margin-top: 2px;
}

.card-body {
    font-size: 0.9375rem;
    color: var(--ink-2);
    line-height: 1.65;
    margin-top: 12px;
}

.card-body ul {
    padding-left: 20px;
    margin-top: 8px;
}

.card-body li {
    margin-bottom: 6px;
}

/* ── Badges ── */
.badge-period {
    display: inline-block;
    padding: 4px 12px;
    background: var(--accent-light);
    color: var(--accent);
    border-radius: 2px;
    font-size: 12px;
    font-weight: 500;
    white-space: nowrap;
}

.badge-status-done {
    display: inline-block;
    padding: 3px 10px;
    background: #edf7f1;
    color: #1a7a42;
    border-radius: 2px;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.04em;
    text-transform: uppercase;
}

.badge-status-active {
    display: inline-block;
    padding: 3px 10px;
    background: #fef9ee;
    color: #9a6b00;
    border-radius: 2px;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.04em;
    text-transform: uppercase;
}

.badge-status-wip {
    display: inline-block;
    padding: 3px 10px;
    background: var(--accent-light);
    color: var(--accent);
    border-radius: 2px;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.04em;
    text-transform: uppercase;
}

/* ── Tags ── */
.tags-row {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-top: 14px;
}

.tag {
    display: inline-block;
    padding: 4px 11px;
    background: var(--surface);
    color: var(--ink-2);
    border: 1px solid var(--rule);
    border-radius: 2px;
    font-size: 12px;
    font-weight: 500;
}

/* ── Skills grid ── */
.skills-group {
    margin-bottom: 28px;
}

.skills-group-title {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--ink-3);
    margin-bottom: 10px;
    padding-bottom: 6px;
    border-bottom: 1px solid var(--rule);
}

/* ── Progress bars ── */
.prog-row {
    margin-bottom: 18px;
}

.prog-header {
    display: flex;
    justify-content: space-between;
    font-size: 0.875rem;
    font-weight: 500;
    color: var(--ink);
    margin-bottom: 6px;
}

.prog-track {
    height: 3px;
    background: var(--rule);
    border-radius: 2px;
    overflow: hidden;
}

.prog-fill {
    height: 100%;
    background: var(--accent);
    border-radius: 2px;
}

/* ── Project links ── */
.proj-links {
    display: flex;
    gap: 8px;
    margin-top: 16px;
    flex-wrap: wrap;
}

.proj-link {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    padding: 7px 14px;
    border: 1px solid var(--rule);
    border-radius: var(--radius);
    color: var(--ink-2) !important;
    text-decoration: none !important;
    font-size: 12px;
    font-weight: 500;
    transition: border-color 0.2s, color 0.2s;
}

.proj-link:hover {
    border-color: var(--accent-mid);
    color: var(--accent) !important;
}

/* ── Contact grid ── */
.contact-item {
    display: flex;
    align-items: flex-start;
    gap: 14px;
    padding: 16px 0;
    border-bottom: 1px solid var(--rule);
}

.contact-item:last-child { border-bottom: none; }

.contact-icon {
    width: 36px;
    height: 36px;
    border-radius: var(--radius);
    background: var(--accent-light);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    font-size: 16px;
}

.contact-label {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--ink-3);
    margin-bottom: 2px;
}

.contact-val {
    font-size: 0.9375rem;
    color: var(--ink);
}

/* ── Streamlit overrides ── */
.stTabs [data-baseweb="tab-list"] {
    gap: 0;
    border-bottom: 1px solid var(--rule);
    background: var(--white);
    padding: 0 60px;
}

.stTabs [data-baseweb="tab"] {
    padding: 14px 22px;
    font-size: 13px;
    font-weight: 500;
    letter-spacing: 0.04em;
    color: var(--ink-3);
    border-bottom: 2px solid transparent;
    transition: color 0.15s, border-color 0.15s;
}

.stTabs [aria-selected="true"] {
    color: var(--accent) !important;
    border-bottom: 2px solid var(--accent) !important;
}

.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    border-radius: var(--radius);
    border: 1px solid var(--rule);
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    padding: 10px 14px;
    background: var(--surface);
    transition: border-color 0.15s;
}

.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: var(--accent-mid);
    box-shadow: 0 0 0 3px rgba(26,58,92,0.07);
    background: var(--white);
}

.stButton > button {
    background: var(--accent);
    color: white;
    border: none;
    border-radius: var(--radius);
    padding: 12px 28px;
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    font-weight: 500;
    letter-spacing: 0.03em;
    width: 100%;
    transition: background-color 0.15s;
}

.stButton > button:hover {
    background: #152e4a;
    border: none;
}

.stSelectbox > div > div {
    border-radius: var(--radius);
    border: 1px solid var(--rule) !important;
    background: var(--surface);
    font-size: 14px;
}
</style>
""",
    unsafe_allow_html=True,
)

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
    st.markdown('<div class="body-wrapper">', unsafe_allow_html=True)

    col_bio, col_offers = st.columns([3, 2], gap="large")

    with col_bio:
        st.markdown(
            f"""
        <div class="section-kicker">Background</div>
        <div class="section-title">About me</div>
        <div class="card">
            <p class="card-body">{cv_data['bio']}</p>
            <div class="tags-row" style="margin-top: 20px;">
                <span class="tag">Open to work</span>
                <span class="tag">Data Science</span>
                <span class="tag">ML Engineering</span>
                <span class="tag">Research</span>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col_offers:
        st.markdown(
            """
        <div class="section-kicker">What I bring</div>
        <div class="section-title">Core strengths</div>
        """,
            unsafe_allow_html=True,
        )

        strengths = [
            ("AI & ML Systems", "Custom models from prototyping through production deployment."),
            ("Data Insight", "Translating messy datasets into clear, actionable decisions."),
            ("End-to-End Delivery", "Full project lifecycle ownership, solo or in a team."),
            ("Communication", "Making technical findings accessible to non-technical audiences."),
        ]

        for title, desc in strengths:
            st.markdown(
                f"""
            <div class="card" style="margin-bottom: 12px; padding: 18px 22px;">
                <div style="font-weight: 600; font-size: 0.9375rem; color: var(--ink); margin-bottom: 4px;">{title}</div>
                <div style="font-size: 0.875rem; color: var(--ink-2); line-height: 1.55;">{desc}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.markdown("</div>", unsafe_allow_html=True)


# ──────────────────────────
# TAB 2 — RÉSUMÉ
# ──────────────────────────
with tab_resume:
    st.markdown('<div class="body-wrapper">', unsafe_allow_html=True)

    # Education
    st.markdown(
        """
    <div class="section-kicker">Academic history</div>
    <div class="section-title">Education</div>
    """,
        unsafe_allow_html=True,
    )

    edu_cols = st.columns(2, gap="medium")
    for col, edu in zip(edu_cols, cv_data["education"]):
        with col:
            highlights_html = "".join(f"<li>{h}</li>" for h in edu["highlights"])
            st.markdown(
                f"""
            <div class="card">
                <div class="card-meta">
                    <div>
                        <div class="card-title">{edu['degree']}</div>
                        <div class="card-sub">{edu['institution']}</div>
                    </div>
                    <span class="badge-period">{edu['period']}</span>
                </div>
                <div style="font-size: 13px; font-weight: 600; color: var(--accent); margin: 10px 0 4px;">{edu['grade']}</div>
                <div class="card-body">
                    <ul>{highlights_html}</ul>
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    # Experience
    st.markdown(
        """
    <div class="section-kicker" style="margin-top: 24px;">Work history</div>
    <div class="section-title">Experience</div>
    """,
        unsafe_allow_html=True,
    )

    for exp in cv_data["experience"]:
        points_html = "".join(f"<li>{p}</li>" for p in exp["points"])
        st.markdown(
            f"""
        <div class="card">
            <div class="card-meta">
                <div>
                    <div class="card-title">{exp['title']}</div>
                    <div class="card-sub">{exp['org']}</div>
                </div>
                <span class="badge-period">{exp['period']}</span>
            </div>
            <div class="card-body">
                <ul>{points_html}</ul>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)


# ──────────────────────────
# TAB 3 — PROJECTS
# ──────────────────────────
with tab_projects:
    st.markdown('<div class="body-wrapper">', unsafe_allow_html=True)

    st.markdown(
        """
    <div class="section-kicker">Selected work</div>
    <div class="section-title">Projects</div>
    """,
        unsafe_allow_html=True,
    )

    for proj in cv_data["projects"]:
        tags_html = "".join(f'<span class="tag">{t}</span>' for t in proj["tags"])

        status_map = {
            "Completed": "badge-status-done",
            "Active": "badge-status-active",
            "In Progress": "badge-status-wip",
        }
        badge_cls = status_map.get(proj["status"], "badge-status-wip")

        st.markdown(
            f"""
        <div class="card">
            <div class="card-meta">
                <div>
                    <div class="card-title">{proj['title']}</div>
                </div>
                <span class="{badge_cls}">{proj['status']}</span>
            </div>
            <div class="card-body" style="margin-top: 8px;">{proj['summary']}</div>
            <div class="tags-row">{tags_html}</div>
            <div class="proj-links">
                <a href="{proj['github']}" target="_blank" class="proj-link">↗ View code</a>
                <a href="{proj['kaggle']}" target="_blank" class="proj-link">◈ Kaggle notebook</a>
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
    st.markdown('<div class="body-wrapper">', unsafe_allow_html=True)

    col_cats, col_prof = st.columns([3, 2], gap="large")

    with col_cats:
        st.markdown(
            """
        <div class="section-kicker">Technical toolkit</div>
        <div class="section-title">Skills by category</div>
        """,
            unsafe_allow_html=True,
        )

        for category, items in cv_data["skills"].items():
            tags_html = "".join(f'<span class="tag">{item}</span>' for item in items)
            st.markdown(
                f"""
            <div class="skills-group">
                <div class="skills-group-title">{category}</div>
                <div class="tags-row" style="margin-top: 0;">{tags_html}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    with col_prof:
        st.markdown(
            """
        <div class="section-kicker">Self-assessed</div>
        <div class="section-title">Proficiency</div>
        """,
            unsafe_allow_html=True,
        )

        for skill, level in cv_data["proficiency"]:
            st.markdown(
                f"""
            <div class="prog-row">
                <div class="prog-header">
                    <span>{skill}</span>
                    <span style="color: var(--ink-3); font-weight: 400;">{level}%</span>
                </div>
                <div class="prog-track">
                    <div class="prog-fill" style="width: {level}%;"></div>
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
    st.markdown('<div class="body-wrapper">', unsafe_allow_html=True)

    col_info, col_form = st.columns([2, 3], gap="large")

    with col_info:
        st.markdown(
            """
        <div class="section-kicker">Get in touch</div>
        <div class="section-title">Contact</div>
        """,
            unsafe_allow_html=True,
        )

        contact_items = [
            ("✉", "Email", f'<a href="mailto:{c["email"]}" style="color: var(--accent);">{c["email"]}</a>'),
            ("📱", "Phone", c["phone"]),
            ("◎", "Location", c["location"]),
            ("⌥", "GitHub", f'<a href="{c["github"]}" target="_blank" style="color: var(--accent);">{c["github"].replace("https://", "")}</a>'),
            ("↗", "LinkedIn", f'<a href="{c["linkedin"]}" target="_blank" style="color: var(--accent);">{c["linkedin"].replace("https://", "")}</a>'),
        ]

        items_html = ""
        for icon, label, val in contact_items:
            items_html += f"""
            <div class="contact-item">
                <div class="contact-icon">{icon}</div>
                <div>
                    <div class="contact-label">{label}</div>
                    <div class="contact-val">{val}</div>
                </div>
            </div>
            """

        st.markdown(f'<div class="card">{items_html}</div>', unsafe_allow_html=True)

    with col_form:
        st.markdown(
            """
        <div class="section-kicker">Send a message</div>
        <div class="section-title">Say hello</div>
        """,
            unsafe_allow_html=True,
        )

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
                    st.session_state.contact_submissions.append(
                        {
                            "name": name,
                            "email": email,
                            "subject": subject,
                            "message": message,
                            "timestamp": datetime.now().isoformat(),
                        }
                    )
                    st.success(f"Message received — thank you, {name}. I'll be in touch soon.")
                else:
                    st.warning("Please complete all fields before sending.")

    st.markdown("</div>", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────
st.markdown(
    f"""
<div style="border-top: 1px solid #e4e4e4; padding: 32px 60px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; background: #f8f7f5;">
    <div style="font-family: 'DM Serif Display', serif; font-size: 1.1rem; color: #1a1a1a;">
        {cv_data['name']}
        <span style="font-family: 'DM Sans', sans-serif; font-size: 0.8rem; font-weight: 400; color: #8a8a8a; margin-left: 10px;">{cv_data['title']}</span>
    </div>
    <div style="font-size: 12px; color: #8a8a8a;">
        © {datetime.now().year} · Kimberley, South Africa
    </div>
</div>
""",
    unsafe_allow_html=True,
)
