# main.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import time

app = FastAPI(
    title="AetherMind API",
    description="AetherMind Free Preview backend",
    version="0.1"
)

# --- CORS (for MVP allow all; tighten later to your Netlify domain)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],            # change to your Netlify domain later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    prompt: str

# Simple demo rate limit (in-memory)
requests_today = 0
last_reset = time.time()

# Friendly homepage
@app.get("/", response_class=HTMLResponse)
def read_root():
    html = """
    <!doctype html>
    <html>
      <head>
        <meta charset="utf-8" />
        <title>AetherMind API</title>
        <meta name="viewport" content="width=device-width,initial-scale=1" />
      </head>
      <body style="font-family: Arial, sans-serif; text-align:center; padding:40px;">
        <h1>AetherMind API</h1>
        <p>Welcome to the AetherMind Free Preview backend.</p>
        <p><a href="/docs">Open API docs (Swagger UI)</a></p>
        <p><a href="/redoc">Open API docs (ReDoc)</a></p>
        <p><a href="/health">Health check</a></p>
      </body>
    </html>
    """
    return HTMLResponse(content=html, status_code=200)

# Simple health endpoint
@app.get("/health")
def health():
    return {"status": "ok"}

# Avoid 404 noise for favicon requests
@app.get("/favicon.ico")
def favicon():
    return Response(status_code=204)

# Demo core endpoint
@app.post("/generate")
def generate_code(query: Query):
    global requests_today, last_reset
    if time.time() - last_reset > 86400:
        requests_today = 0
        last_reset = time.time()
    if requests_today > 50:
        raise HTTPException(status_code=429, detail="Free quota exceeded, come back tomorrow")
    requests_today += 1

    # Replace this with your actual AetherMind integration
    return {"output": f"AetherMind simulated response for: {query.prompt}"}
