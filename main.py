from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from apps.calculator.route import router as calculator_router
from constants import SERVER_URL, PORT, ENV
import google.generativeai as genai
import os
from apps.auth.route import auth_router


app = FastAPI()

origins = [
    "http://localhost:5173",  # React Vite Dev Server
    "https://ai-notes-topaz-one.vercel.app",  # Your Vercel frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # Required if using authentication cookies
    allow_methods=["*"],  # ✅ Allow ALL HTTP methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # ✅ Allow ALL headers
)

@app.get("/")
async def root():
    return {
        "message": "Apka is nagri me swagat hai!\n",
        "version": "1.0.0",
        "docs": "/docs"  
    }

# @/calculate
app.include_router(calculator_router)
app.include_router(auth_router)


