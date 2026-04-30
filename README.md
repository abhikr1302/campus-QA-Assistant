# 🎓 Campus Event Q&A Assistant (GenAI)

A GenAI-powered assistant that answers student queries about campus events using the Google Gemini API with structured outputs.

---

## 🚀 Overview

This project demonstrates how to build an intelligent assistant that:

- Answers campus event-related questions
- Returns structured JSON responses for event queries
- Handles off-topic queries conversationally
- Uses prompt engineering to control LLM output

---

## ✨ Features

- 🔍 Event-based Q&A (Tech Fest, Career Fair, Hackathon, etc.)
- 📦 Strict JSON output format for event queries
- 💬 Conversational responses for non-event queries
- ⚡ Powered by Google Gemini API
- 🌐 Streamlit web interface
- 🔐 Secure API key handling using `.env`

---

## 🧠 How It Works

1. User enters a query
2. System prompt provides event database context
3. Gemini model processes the query
4. Output is returned as:
   - JSON → for event queries
   - Plain text → for non-event queries

---

## 📊 Example Outputs

### ✅ Event Query

Input:
When is the Tech Fest happening?

Output:
{
  "event_name": "Tech Fest",
  "date": "2025-09-15",
  "location": "Main Auditorium",
  "response": "The Tech Fest will be held on 15th September at the Main Auditorium."
}

---

### 💬 Non-Event Query

Input:
Tell me a joke

Output:
Sure! Here's one: Why don't programmers like nature? It has too many bugs!

---

## 🏗 Project Structure

campus-event-qa-assistant/
│
├── app.py
├── main.py
├── prompt.txt
├── requirements.txt
├── .env (not included in repo)
│
└── utils/
    ├── __init__.py
    └── config.py

---

## ⚙️ Setup Instructions

1. Clone Repository

git clone https://github.com/your-username/campus-event-qa-assistant.git  
cd campus-event-qa-assistant

---

2. Install Dependencies

pip install -r requirements.txt

---

3. Add API Key

Create a .env file in the project root:

GEMINI_API_KEY=your_api_key_here

Get your API key from:
https://aistudio.google.com/app/apikey

---

4. Run Application

python -m streamlit run app.py

---

## 🛠 Tech Stack

- Python
- Google Gemini API
- Streamlit
- dotenv

---

## 🎯 Use Cases

- Campus assistants
- Student helpdesk systems
- Event information bots

---

## 🚧 Future Improvements

- JSON schema validation
- Intent classification layer
- Chat history memory
- Deployment (Streamlit Cloud / Docker)
- UI improvements (chat interface)

---

## 👨‍💻 Author

Abhishek Kumar  
Data Analyst | ML & GenAI Enthusiast  

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
