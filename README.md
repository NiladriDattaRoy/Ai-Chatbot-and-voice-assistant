AI Chatbot with Voice & News Reader

This project is an AI-powered chatbot built using FastAPI for the backend and a Telegram-inspired UI for the frontend.
It can answer FAQs, fetch and read the latest news headlines, and speak responses using Text-to-Speech (TTS).

🚀 Features

✅ FAQ Support – Answers common questions from a JSON file.

✅ News Reader – Fetches top 5 latest news headlines (Google News RSS).

✅ Text-to-Speech (TTS) – Speaks responses using a female voice.

✅ Interactive UI – Clean, wide chatbox styled like Telegram.

✅ Single Script – Backend + Frontend (HTML, CSS, JS) in one Python file.

📂 Project Structure

Everything is inside a single file:

app.py   # FastAPI backend + chatbot logic + frontend HTML/CSS/JS

⚙️ Installation

Clone or download this project.

Install required dependencies:

pip install fastapi uvicorn pyttsx3 feedparser


Run the chatbot:

python app.py


Open in browser:

http://127.0.0.1:8000/

🎤 How It Works

Type a question like:

What is your name?

How are you?

Can you read news?

If the question matches the FAQ, the chatbot answers and speaks aloud.

If you ask for news, it fetches and reads the top 5 headlines one by one.

If it doesn’t understand, it politely tells you it will pass the query to a human agent.

🖼️ UI Preview

Modern Telegram-like design.

Wide chatbox for better readability.

User messages (green) appear on the right.

Bot messages (gray) appear on the left.

🛠️ Tech Stack

Backend: FastAPI (Python)

Frontend: HTML, CSS, JavaScript (served from backend)

Text-to-Speech: pyttsx3

News API: Google News RSS via feedparser

📌 Notes

Currently configured for a female voice (Windows SAPI5).

To add more voices, install language packs in Windows settings.

Works best on Python 3.8+.
