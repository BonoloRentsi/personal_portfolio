import streamlit as st
from datetime import datetime

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Portfolio | Data Scientist",
    page_icon="◈",
    layout="wide"
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
        "location": "South Africa",
        "github": "https://github.com/yourname",
        "linkedin": "https://www.linkedin.com/in/yourname",
        "kaggle": "https://www.kaggle.com/yourname",
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
                "Provide academic guidance and study support to students",
                "Develop workshop materials and study resources",
            ],
        },
        {
            "title": "Academic Support Specialist",
            "org": "Sol Plaatje University",
            "period": "Jan 2025 – Present",
            "points": [
                "Tutored across core data science modules",
                "Mentored students through research projects",
            ],
        },
    ],
    "projects": [
        {
            "title": "Skin Disease Detection",
            "summary": "CNN-based classifier for dermatological conditions.",
            "tags": ["Python", "TensorFlow", "CNN"],
            "github": "https://github.com/",
            "kaggle": "https://www.kaggle.com/",
            "status": "Completed",
        },
        {
            "title": "Network Traffic Anomaly Detection",
            "summary": "Intrusion detection system using ML.",
            "tags": ["Python", "Scikit-learn", "Cybersecurity"],
            "github": "https://github.com/",
            "kaggle": "https://www.kaggle.com/",
            "status": "Active",
        },
    ],
    "skills": {
        "Programming": ["Python", "R", "SQL", "C++"],
        "Machine Learning": ["Scikit-learn", "XGBoost", "TensorFlow", "PyTorch"],
        "Data & Analytics": ["Pandas", "NumPy", "Spark"],
        "Visualisation": ["Tableau", "Power BI", "Plotly"],
    },
    "proficiency": [
        ("Python", 95),
        ("Machine Learning", 90),
        ("SQL", 85),
        ("Deep Learning", 82),
    ],
}

# ─────────────────────────────────────────────
# HERO
# ─────────────────────────────────────────────
c = cv_data["contact"]

st.markdown(f"""
# {cv_data['name']}
### {cv_data['title']}
{cv_data['tagline']}

📧 {c['email']} | 🌍 {c['location']}  
[GitHub]({c['github']}) | [LinkedIn]({c['linkedin']}) | [Kaggle]({c['kaggle']})
""")

st.divider()

# ─────────────────────────────────────────────
# TABS
# ─────────────────────────────────────────────
tab_about, tab_resume, tab_projects, tab_skills, tab_contact = st.tabs(
    ["About", "Résumé", "Projects", "Skills", "Contact"]
)

# ABOUT
with tab_about:
    st.subheader("About Me")
    st.write(cv_data["bio"])

# RESUME
with tab_resume:
    st.subheader("Education")
    for edu in cv_data["education"]:
        st.markdown(f"""
**{edu['degree']}**  
{edu['institution']} | {edu['period']}  
Grade: {edu['grade']}
""")
        for h in edu["highlights"]:
            st.write("•", h)
        st.write("")

    st.subheader("Experience")
    for exp in cv_data["experience"]:
        st.markdown(f"""
**{exp['title']}**  
{exp['org']} | {exp['period']}
""")
        for p in exp["points"]:
            st.write("•", p)
        st.write("")

# PROJECTS
with tab_projects:
    for proj in cv_data["projects"]:
        st.subheader(proj["title"])
        st.write(proj["summary"])
        st.write("Technologies:", ", ".join(proj["tags"]))
        st.write(f"[GitHub]({proj['github']}) | [Kaggle]({proj['kaggle']})")
        st.divider()

# SKILLS
with tab_skills:
    st.subheader("Skills")
    for category, items in cv_data["skills"].items():
        st.write(f"**{category}:** {', '.join(items)}")

    st.subheader("Proficiency")
    for skill, level in cv_data["proficiency"]:
        st.write(skill)
        st.progress(level / 100)

# CONTACT
with tab_contact:
    st.subheader("Contact Form")

    with st.form("contact_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        name = col1.text_input("Name")
        email = col2.text_input("Email")

        subject = st.selectbox(
            "Subject",
            ["Select subject", "Job opportunity", "Project inquiry", "Collaboration", "Question", "Other"]
        )

        message = st.text_area("Message")

        submitted = st.form_submit_button("Send Message")

        if submitted:
            if name and email and subject != "Select subject" and message:
                st.session_state.contact_submissions.append({
                    "name": name,
                    "email": email,
                    "subject": subject,
                    "message": message,
                    "timestamp": datetime.now().isoformat(),
                })
                st.success("Message sent successfully!")
            else:
                st.warning("Please fill in all fields.")

# FOOTER
st.divider()
st.write(f"© {datetime.now().year} {cv_data['name']} | Data Scientist")
