🚀 Resume Job Matcher (RAG-based AI System)

An AI-powered application that matches resumes with job descriptions using Retrieval-Augmented Generation (RAG). It analyzes compatibility, identifies skill gaps, and provides actionable suggestions using a combination of semantic search and LLM reasoning.

📌 Overview

This project simulates an intelligent hiring assistant by combining vector search (FAISS) with a Llama-based LLM (via Groq API). It processes resumes and job descriptions, evaluates their alignment, and generates structured insights such as match score, missing skills, strengths, and improvement suggestions.

✨ Features
📄 Upload Resume (PDF)
📝 Input Job Description
🔍 Semantic Similarity Matching
🎯 AI-generated Match Score (0–100)
❌ Skill Gap Identification
💡 Personalized Suggestions
🖥️ Interactive UI using Streamlit
🧠 How It Works
Resume is parsed from PDF
Job descriptions are processed
Text is converted into embeddings using Sentence Transformers
FAISS retrieves relevant matches
LLM analyzes resume vs job description
Structured output is generated
🛠️ Tech Stack
Python
LangChain
FAISS (Vector Database)
Sentence Transformers
Groq API (Llama 3 Model)
Streamlit

