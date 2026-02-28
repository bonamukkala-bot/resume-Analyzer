
# 🚀 AI Resume Analyzer

### Intelligent Resume vs Job Description Matching System

> A smart AI-powered web application that compares a resume with a job description and generates a match score, identifies missing skills, and suggests improvements — similar to how real ATS systems work.

---

## 📌 Project Overview

The **AI Resume Analyzer** is a real-world AI application built using Python and Streamlit.

It allows users to:

* Upload a resume (PDF)
* Paste a job description
* Get an AI-generated analysis report

The system uses an AI model via API to analyze both documents and provide structured feedback.

This project demonstrates:

* API integration
* Prompt engineering
* File handling
* Web application development
* Secure environment management

---

## 🎯 Features

* 📄 Upload Resume (PDF)
* 📝 Paste Job Description
* 📊 Match Percentage
* ❌ Missing Skills Detection
* 💡 Resume Improvement Suggestions
* 🌐 Simple and Clean Web Interface

---

## 🧠 How It Works

1. User uploads resume (PDF format).
2. The system extracts readable text from the PDF.
3. User pastes job description.
4. Resume text and job description are sent to an AI model.
5. AI analyzes and returns:

   * Match percentage
   * Missing skills
   * Suggestions
6. Results are displayed in the web application.

---

# 🗂 Project Structure

ai-resume-analyzer/

* app.py → Main application (Streamlit UI)
* analyzer.py → AI API communication logic
* utils.py → PDF text extraction logic
* requirements.txt → Required libraries
* .env → API key storage (not uploaded to GitHub)
* README.md → Project documentation

---

# 📁 File Explanation

## 1️⃣ app.py – Main Application

This file:

* Builds the web interface
* Takes user inputs (resume + job description)
* Calls the AI analyzer
* Displays the result

It connects all parts of the project together.

---

## 2️⃣ analyzer.py – AI Processing Logic

This file:

* Loads API key securely
* Creates structured AI prompt
* Sends request to AI model
* Receives and processes AI response
* Returns formatted result

This is the **brain of the project**.

---

## 3️⃣ utils.py – PDF Text Extraction

This file:

* Opens the uploaded PDF
* Extracts text page by page
* Combines the text
* Returns clean text

This converts the resume into readable text for AI.

---

## 4️⃣ requirements.txt – Dependencies

Contains all required Python libraries so others can install everything easily.

---

## 5️⃣ .env – Secure API Key Storage

Stores your API key safely.

⚠️ This file should NOT be uploaded to GitHub.

---

# ⚙️ Installation Guide (Step-by-Step)

Follow these steps to run the project locally.

---

## 🔹 Step 1: Install Python

Download Python from:

[https://www.python.org/downloads/](https://www.python.org/downloads/)

After installing, verify:

```
python --version
```

You should see something like:

Python 3.x.x

---

## 🔹 Step 2: Clone the Repository (or Create Folder)

If using GitHub:

```
git clone https://github.com/your-username/ai-resume-analyzer.git
cd ai-resume-analyzer
```

Or manually create folder:

```
mkdir ai-resume-analyzer
cd ai-resume-analyzer
```

---

## 🔹 Step 3: Create Virtual Environment (Recommended)

```
python -m venv venv
```

Activate it:

### Windows

```
venv\Scripts\activate
```

### Mac/Linux

```
source venv/bin/activate
```

---

## 🔹 Step 4: Install Required Libraries

If you have `requirements.txt`:

```
pip install -r requirements.txt
```

Or install manually:

```
pip install streamlit requests pdfplumber python-dotenv
```

---

## 🔹 Step 5: Add Your API Key

Create a file named `.env`

Add:

```
OPENROUTER_API_KEY=your_api_key_here
```

⚠️ Do not upload this file to GitHub.

Create `.gitignore` file and add:

```
.env
venv/
__pycache__/
```

---

## ▶️ Step 6: Run the Application

Start the Streamlit server:

```
streamlit run app.py
```

After running, open your browser and go to:

```
http://localhost:8501
```

Your AI Resume Analyzer will be live 🎉

---

# 🏗 Technologies Used

* Python
* Streamlit
* OpenRouter API
* Mistral 7B Model
* pdfplumber
* python-dotenv

---

# 🎓 What You Learn From This Project

* Real API integration
* Prompt engineering
* PDF handling in Python
* Building web apps with Streamlit
* Secure API key management
* Modular project structure

---

# 🚀 Future Improvements

* Graphical skill match visualization
* Downloadable PDF report
* Resume keyword highlighting
* Resume rewriting suggestions
* Deploy to Streamlit Cloud
* Multi-model AI selection



Just tell me 🚀
