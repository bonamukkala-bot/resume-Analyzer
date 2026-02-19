import streamlit as st
from utils import extract_text_from_pdf
from analyzer import analyze_resume

st.set_page_config(page_title="AI Resume Analyzer")

st.title("📄 AI Resume Analyzer (Gemini Version)")

st.write("Upload your resume (PDF) and paste the job description.")

# Upload Resume
uploaded_file = st.file_uploader("Upload Resume (PDF only)", type=["pdf"])

# Job Description
job_description = st.text_area("Paste Job Description Here")

if st.button("Analyze Resume"):

    if uploaded_file is not None and job_description.strip() != "":

        with st.spinner("Analyzing your resume... Please wait..."):

            resume_text = extract_text_from_pdf(uploaded_file)

            result = analyze_resume(resume_text, job_description)

        st.subheader("📊 Analysis Result")
        st.write(result)

    else:
        st.warning("Please upload resume and enter job description.")
