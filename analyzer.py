import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = "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"
print("Loaded API Key:", API_KEY)


def analyze_resume(resume_text, job_description):

    prompt = f"""
    You are an expert HR professional.

    Compare the resume and job description.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Give:
    1. Match percentage
    2. Missing skills
    3. Suggestions to improve resume
    """

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "mistralai/mistral-7b-instruct",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )

    # Convert to JSON
    result = response.json()

    # Debug print (important)
    print("API Response:", result)

    # Check if request successful
    if "choices" in result:
        return result["choices"][0]["message"]["content"]
    else:
        return f"API Error: {result}"
