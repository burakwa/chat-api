from fastapi import FastAPI
from app.api.routes.chat import router as chat_router

app = FastAPI(
    title="Professional Chat API",
    description="OOP prensiplerine uygun, genişletilebilir Chat API mimarisi.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(chat_router)
@app.get("/", tags=["Health Check"])
async def root():
    return {"status": "alive", "message": "Chat API is running smoothly."}
