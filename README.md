# 🌍 AI Agents – Weather & Time Chatbot

This project demonstrates an AI agent using **[Google ADK](https://github.com/google/adk)** that answers questions about **weather** and **current time** in any city.

Powered by:
- 🌐 OpenWeatherMap API (Current Weather + Geocoding)
- 🕒 Python `timezonefinder` + `zoneinfo`
- 🤖 Google ADK Agent Framework

---

## 🧠 What It Does

A conversational AI agent that responds to queries like:
- _"What's the weather like in Tokyo?"_
- _"What time is it in Berlin?"_

It uses:
- `get_weather(city)` → fetches real-time weather data via OpenWeatherMap
- `get_current_time(city)` → fetches timezone-aware local time using geolocation

---

## 🚀 Live Chatbot

Using the [ADK Web](https://github.com/google/adk-web) interface, this project creates an interactive chatbot with the tools registered as agent functions.

---

## 🛠️ Setup

### 1. Clone the Repo

```bash
git clone https://github.com/navjsingh/AI_agents.git
cd AI_agents
```
### 2. Create a .env File

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
OPENWEATHER_API_KEY=your_actual_openweather_api_key_here
```

### 3. Create & Activate Virtual Environment (Recommended):

# Create
```python -m venv .venv```
# Activate (each new terminal)
# macOS/Linux: 
```source .venv/bin/activate```
# Windows CMD: 
```.venv\Scripts\activate.bat```
# Windows PowerShell: 
```.venv\Scripts\Activate.ps1```

### 4. Install Dependencies

```
pip install -r requirements.txt
```

### 5. Run the Agent (via ADK Web)

```
adk web
```
