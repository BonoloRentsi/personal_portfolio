import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Bonolo Rentsi | AI Researcher",
    page_icon="🧠",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

html, body, [class*="css"]{
    font-family: 'Inter', sans-serif;
}

.stApp{
    background-color:#0B1120;
}

section.main{
    background-color:#0B1120;
}

.hero{
    padding-top:100px;
    padding-bottom:100px;
}

.name{
    font-size:70px;
    font-weight:800;
    color:white;
}

.title{
    font-size:26px;
    color:#38BDF8;
    font-weight:600;
}

.tagline{
    font-size:20px;
    color:#CBD5E1;
    max-width:700px;
}

.section-title{
    font-size:42px;
    font-weight:800;
    color:white;
    margin-top:60px;
    margin-bottom:30px;
}

.card{
    background:#111827;
    padding:25px;
    border-radius:20px;
    border:1px solid #1E293B;
}

.skill{
    display:inline-block;
    background:#1E293B;
    color:white;
    padding:10px 16px;
    border-radius:10px;
    margin:5px;
}

.project-card{
    background:#111827;
    padding:25px;
    border-radius:20px;
    margin-bottom:20px;
    border:1px solid #1E293B;
}

.project-title{
    font-size:24px;
    color:white;
    font-weight:700;
}

.project-desc{
    color:#CBD5E1;
}

.footer{
    text-align:center;
    color:#94A3B8;
    margin-top:50px;
    padding:20px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HERO
# --------------------------------------------------

st.markdown("""
<div class="hero">

<div class="title">
AI Researcher • Data Scientist • ML Engineer
</div>

<div class="name">
Bonolo Rentsi
</div>

<div class="tagline">
Building intelligent systems that transform data into
real-world solutions using Artificial Intelligence,
Deep Learning, Computer Vision, Explainable AI,
and Federated Learning.
</div>

</div>
""", unsafe_allow_html=True)

col1,col2,col3=st.columns(3)

with col1:
    st.link_button("GitHub","https://github.com/placeholder")

with col2:
    st.link_button("LinkedIn","https://linkedin.com/in/placeholder")

with col3:
    st.link_button("Download CV","#")

st.divider()

# --------------------------------------------------
# ABOUT
# --------------------------------------------------

st.markdown(
    '<div class="section-title">About Me</div>',
    unsafe_allow_html=True
)

col1,col2 = st.columns([1,2])

with col1:
    st.image(
        "https://images.unsplash.com/photo-1500648767791-00dcc994a43",
        width=300
    )

with col2:
    st.write("""
    I am a passionate Data Scientist and AI Researcher
    currently pursuing a Master's degree in Data Science.

    My work focuses on:

    • Artificial Intelligence

    • Explainable AI

    • Deep Learning

    • Computer Vision

    • Healthcare Analytics

    • Federated Learning

    • Astronomy & Space Weather Prediction

    I enjoy transforming complex data into intelligent,
    impactful solutions.
    """)

# --------------------------------------------------
# EDUCATION
# --------------------------------------------------

st.markdown(
    '<div class="section-title">Education</div>',
    unsafe_allow_html=True
)

st.markdown("""
### 🎓 MSc Data Science
**Sol Plaatje University**  
2026 – Present

---

### 🎓 BSc Honours Data Science
**Sol Plaatje University**  
2025

Average: 76%

---

### 🎓 BSc Data Science
**Sol Plaatje University**  
2022 – 2024

Average: 81%
""")

# --------------------------------------------------
# RESEARCH INTERESTS
# --------------------------------------------------

st.markdown(
    '<div class="section-title">Research Interests</div>',
    unsafe_allow_html=True
)

research = [
    "Artificial Intelligence",
    "Explainable AI",
    "Federated Learning",
    "Computer Vision",
    "Healthcare Analytics",
    "Speech Emotion Recognition",
    "Deep Learning",
    "Astronomy",
    "Space Weather Prediction",
    "Machine Learning"
]

for r in research:
    st.markdown(
        f'<span class="skill">{r}</span>',
        unsafe_allow_html=True
    )

# --------------------------------------------------
# FEATURED PROJECTS
# --------------------------------------------------

st.markdown(
    '<div class="section-title">Featured Projects</div>',
    unsafe_allow_html=True
)

projects = [
    {
        "title":"Monkeypox Detection using Deep Learning",
        "description":"CNNs, Vision Transformers, Explainable AI and Federated Learning for medical image classification."
    },
    {
        "title":"Emotion Detection from Speech",
        "description":"LSTM, GRU and CNN-RNN architectures for emotion recognition from audio recordings."
    },
    {
        "title":"Solar Flare Prediction",
        "description":"Machine Learning models for predicting solar flare events using space weather data."
    },
    {
        "title":"Career Compass",
        "description":"AI-powered career guidance and recommendation platform."
    },
    {
        "title":"Network Intrusion Detection",
        "description":"Real-time anomaly detection system for network traffic."
    },
    {
        "title":"Drug Recommendation System",
        "description":"Hybrid recommendation engine using collaborative and content-based filtering."
    }
]

for project in projects:

    st.markdown(f"""
    <div class="project-card">

    <div class="project-title">
    {project['title']}
    </div>

    <br>

    <div class="project-desc">
    {project['description']}
    </div>

    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# EXPERIENCE
# --------------------------------------------------

st.markdown(
    '<div class="section-title">Experience</div>',
    unsafe_allow_html=True
)

st.markdown("""
### Academic Support Specialist
Sol Plaatje University

- Tutored Data Science modules
- Supported student research
- Developed learning resources

---

### Peer Mentor
Sol Plaatje University

- Mentored undergraduate students
- Academic guidance and support
- Workshop facilitation

---

### Teaching Assistant
Homevale High School

- STEM support
- Mathematics tutoring
- Computer Science instruction
""")

# --------------------------------------------------
# SKILLS
# --------------------------------------------------

st.markdown(
    '<div class="section-title">Technical Skills</div>',
    unsafe_allow_html=True
)

skills = {
    "Programming":
        ["Python","R","SQL","C++"],

    "Machine Learning":
        ["TensorFlow","PyTorch","XGBoost","Scikit-Learn"],

    "Data Analysis":
        ["Pandas","NumPy","Spark"],

    "Visualization":
        ["Power BI","Tableau","Plotly"],

    "Cloud & DevOps":
        ["Docker","Git","AWS","Linux"]
}

for category,items in skills.items():

    st.subheader(category)

    for item in items:
        st.markdown(
            f'<span class="skill">{item}</span>',
            unsafe_allow_html=True
        )

# --------------------------------------------------
# ACHIEVEMENTS
# --------------------------------------------------

st.markdown(
    '<div class="section-title">Achievements</div>',
    unsafe_allow_html=True
)

st.markdown("""
🏆 BSc Data Science – 81% Average

🏆 BSc Honours Data Science – 76% Average

🏆 Multiple AI Healthcare Projects

🏆 Academic Tutor & Mentor

🏆 Research in Explainable AI and Federated Learning

🏆 Deep Learning Researcher
""")

# --------------------------------------------------
# CONTACT
# --------------------------------------------------

st.markdown(
    '<div class="section-title">Contact</div>',
    unsafe_allow_html=True
)

st.write("""
Let's build something impactful together.
""")

name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")

if st.button("Send Message"):
    st.success("Message sent successfully!")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("""
<div class="footer">

© 2026 Bonolo Rentsi

AI Researcher • Data Scientist • Machine Learning Engineer

Johannesburg, South Africa

</div>
""", unsafe_allow_html=True)