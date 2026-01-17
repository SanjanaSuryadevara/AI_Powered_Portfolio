import streamlit as st
import google.generativeai as genai
import os
import zipfile
from dotenv import load_dotenv
from io import BytesIO
import PyPDF2
from docx import Document

# --------------------------------------------------
# ENVIRONMENT SETUP
# --------------------------------------------------
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# --------------------------------------------------
# STREAMLIT CONFIG (MUST BE FIRST)
# --------------------------------------------------
st.set_page_config(
    page_title="AI Portfolio Generator",
    page_icon="🎨",
    layout="wide"
)

st.title("🎨 AI-Powered Portfolio Website Generator")
st.caption("Upload your resume → Get a modern portfolio website instantly")

# --------------------------------------------------
# FILE UPLOAD
# --------------------------------------------------
uploaded_file = st.file_uploader(
    "Upload Resume (PDF or DOCX)",
    type=["pdf", "docx"]
)

# --------------------------------------------------
# RESUME TEXT EXTRACTION
# --------------------------------------------------
def extract_text(file):
    text = ""

    if file.name.endswith(".pdf"):
        with BytesIO(file.read()) as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                if page.extract_text():
                    text += page.extract_text() + "\n"

    elif file.name.endswith(".docx"):
        doc = Document(file)
        for para in doc.paragraphs:
            text += para.text + "\n"

    return text.strip()

# --------------------------------------------------
# GENERATE WEBSITE
# --------------------------------------------------
if st.button("🚀 Generate Portfolio Website") and uploaded_file:

    resume_text = extract_text(uploaded_file)

    st.subheader("📄 Resume Preview")
    st.text_area("", resume_text[:4000], height=220)

    prompt = f"""
You are a senior frontend developer and UI/UX designer.

Generate a visually stunning, modern, responsive personal portfolio website.

DESIGN REQUIREMENTS:
- Gradient hero section
- Card-based layout
- Smooth hover animations
- Professional color palette
- Mobile responsive design

STRICT OUTPUT FORMAT (NO EXTRA TEXT):

--html--
Complete HTML (Hero, About, Skills, Projects, Experience, Education, Contact)
--html--

--css--
Modern CSS with gradients, cards, animations
--css--

--js--
Minimal JavaScript (smooth scrolling / interactions)
--js--

Resume Content:
{resume_text}
"""

    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)
        result = response.text

        # ---------------- PARSE OUTPUT ----------------
        html = result.split("--html--")[1].split("--html--")[0].strip()
        css = result.split("--css--")[1].split("--css--")[0].strip()
        js = result.split("--js--")[1].split("--js--")[0].strip()

        # ---------------- SAVE FILES ----------------
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)

        with open("style.css", "w", encoding="utf-8") as f:
            f.write(css)

        with open("script.js", "w", encoding="utf-8") as f:
            f.write(js)

        # ---------------- ZIP FILE ----------------
        with zipfile.ZipFile("portfolio_website.zip", "w") as zipf:
            zipf.write("index.html")
            zipf.write("style.css")
            zipf.write("script.js")

        st.success("✅ Portfolio Website Generated Successfully!")

    except Exception as e:
        st.error("❌ Failed to generate website")
        st.code(str(e))

# --------------------------------------------------
# DOWNLOAD SECTION
# --------------------------------------------------
if os.path.exists("portfolio_website.zip"):
    with open("portfolio_website.zip", "rb") as f:
        st.download_button(
            "⬇ Download Portfolio Website (ZIP)",
            f,
            file_name="portfolio_website.zip",
            mime="application/zip"
        )
