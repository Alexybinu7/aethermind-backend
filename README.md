# AetherMind Backend

🚀 FastAPI backend for **AetherMind Free Preview**, the AI Software Engineer MVP by [AetherSphere](https://aethersphereorg.org).

This backend powers the free demo of AetherMind, handling requests from the frontend and returning AI responses.

---

## 🔹 Features
- Built with [FastAPI](https://fastapi.tiangolo.com/)
- `/generate` endpoint for prompt → response
- Simple daily request limiter (50 free requests/day)
- Ready for deployment on [Render](https://render.com) / [Railway](https://railway.app)

---

## 🔹 Setup (Local)

```bash
# Clone repo
git clone https://github.com/<your-username>/aethermind-backend.git
cd aethermind-backend

# Install dependencies
pip install -r requirements.txt

# Run locally
uvicorn main:app --reload
