# Drive-Thru Service Agent using Google ADK

This repository contains a prototype of a **Drive-Thru Service Agent** built using **Google Agent Development Kit (ADK)**.  
It follows the YouTube tutorial by Mas **Ibnu Sina**:  
[🎥 Tutorial Membuat Aplikasi Drive Thru Menggunakan Agent Development Kit (ADK)](https://www.youtube.com/watch?v=_iW6CY9bki0&t=708s)  

The project is part of my personal preparation for an upcoming **hackathon** Google Cloud Next'25 Bandung.

---

## 🎯 Purpose
- Learn how to develop conversational agents using **Google ADK**.
- Explore real-world use case simulation with a **Drive-Thru ordering flow**.
- Prepare for hackathon challenges involving AI agents.

---

## 🚀 Features
- Greeting, order-taking and confirmation flow.
- Simple modular agent setup for easy customization.
- Local web interface for testing interactions.

---

## 🛠️ Tech Stack
- **Python**
- **Google Agent Development Kit (ADK)**
- Free Google API Key from https://aistudio.google.com/

---

## 📦 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/<username>/<repo-name>.git
   cd <repo-name>

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Run Locally
   ```bash
   python -m uvicorn main:app --host 127.0.0.1 --port 8002 --reload

## 📚 References
- Ibnu Sina’s tutorial video: https://www.youtube.com/watch?v=_iW6CY9bki0&t=708s
- Google ADK Quickstart: https://google.github.io/adk-docs/streaming/custom-streaming-ws/#3.-interact-with-your-streaming-app

## Documentation
- Visulize your Agent
  ```bash
  adk web
![Video3](https://github.com/user-attachments/assets/f674081c-88d7-424a-bf29-2e2054c26e92)
   
