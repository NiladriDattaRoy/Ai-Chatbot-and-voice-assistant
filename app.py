# app.py
from fastapi import FastAPI
from pydantic import BaseModel
import pyttsx3
import datetime
import feedparser
import os
import threading
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or your frontend URL
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# Set female voice (you may need to adjust index for your system)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)

# Speak function
def speak(message):
    """Run pyttsx3 in a separate thread to avoid double speaking."""
    def run():
        engine.say(message)
        engine.runAndWait()
    t = threading.Thread(target=run)
    t.start()

# Pydantic model
class UserMessage(BaseModel):
    user_text: str

# Check if running in reload worker
def is_worker_process():
    return os.environ.get("UVICORN_RELOAD") is None

# Wish function
def wish():
    hour = datetime.datetime.now().hour
    if hour < 12:
        message = "Good Morning!!!"
    elif hour < 18:
        message = "Good Afternoon!!!"
    else:
        message = "Good Evening!!!"

    full_message = f"{message} , how can I help you?"
    
    
    
    speak(full_message)
    return full_message
    

# News function
def get_news():
    try:
        rss_url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
        feed = feedparser.parse(rss_url)
        articles = feed.entries[:5]
        day = ["first", "second", "third", "fourth", "fifth"]

        messages = []
        for i, ar in enumerate(articles):
            news_message = f"Today's {day[i]} news is: {ar['title']}"
            messages.append(news_message)
            if is_worker_process():
                speak(news_message)
        return messages
    except Exception as e:
        return [f"Error fetching news: {e}"]
# Chat route
@app.post("/chat")
async def chatbot(request: UserMessage):
    user_message = request.user_text.lower()

    # Simple keyword handling
    if "hi" in user_message or "hello" in user_message:
        response = wish()
    elif "news" in user_message:
        response = get_news()  # returns list of news
    else:
        response = "Sorry, I don't know that yet — I'll pass this to a human agent."

    return {"response": response, "speak": response}