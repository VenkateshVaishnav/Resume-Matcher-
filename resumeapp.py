import streamlit as st
import os
from pypdf import PdfReader
from langchain_groq import ChatGroq
import json
import re

# 🔑 SET API KEY
os.environ["GROQ_API_KEY"] = "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"

llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    temperature=0
)

# 📄 Load Resume
def load_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# 🤖 LLM Function
def match_resume_to_job(resume, job_desc):
    prompt = f"""
    Compare the resume and job description.

    Resume:
    {resume}

    Job Description:
    {job_desc}

    Return ONLY JSON:
    {{
        "match_score": number (0-100),
        "missing_skills": [],
        "strengths": [],
        "suggestions": []
    }}
    """

    response = llm.invoke(prompt)
    return response.content

# 🧹 Clean Output
def clean_output(output):
    try:
        json_part = re.search(r"\{.*\}", output, re.DOTALL).group()
        return json.loads(json_part)
    except:
        return None

# 🎨 UI
st.title("🚀 Resume Job Matcher")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
job_desc = st.text_area("Paste Job Description")

if st.button("Analyze"):
    if uploaded_file and job_desc:
        resume_text = load_pdf(uploaded_file)

        raw = match_resume_to_job(resume_text, job_desc)
        result = clean_output(raw)

        if result:
            if result["match_score"] <= 1:
                result["match_score"] *= 100

            st.subheader("🎯 Match Score")
            st.success(f"{int(result['match_score'])}%")

            st.subheader("❌ Missing Skills")
            for skill in result["missing_skills"]:
                st.write(f"- {skill}")

            st.subheader("💪 Strengths")
            for s in result["strengths"]:
                st.write(f"- {s}")

            st.subheader("📌 Suggestions")
            for sug in result["suggestions"]:
                st.write(f"- {sug}")
    else:
        st.warning("Please upload resume and paste job description.")