from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import time
from fastapi.middleware.cors import CORSMiddleware   # 👈 NEW IMPORT

app = FastAPI()

# 👇 Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # For MVP: allow all (later restrict to Netlify domain)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    prompt: str

# Simple request limiter (max 50/day for demo)
requests_today = 0
last_reset = time.time()

@app.post("/generate")
def generate_code(query: Query):
    global requests_today, last_reset
    if time.time() - last_reset > 86400:  # reset every 24h
        requests_today = 0
        last_reset = time.time()
    if requests_today > 50:
        raise HTTPException(status_code=429, detail="Free quota exceeded, come back tomorrow")
    requests_today += 1

    # Demo logic (replace with AetherMind model integration)
    return {"output": f"AetherMind simulated response for: {query.prompt}"}
