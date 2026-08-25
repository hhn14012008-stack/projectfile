from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="ProjectFile API",
    description="A web app built with FastAPI",
    version="1.0.0"
)

# Define allowed origins for CORS
origins = [
    "http://localhost:3000",      # Link chạy thử nghiệm ở máy cục bộ (React/Next.js)
    "http://127.0.0.1:3000",
    "https://yourdomain.com",     # Link thật của trang Web Frontend của bạn sau này
    "https://vercel.app"          # Ví dụ link frontend trên Vercel
]

# Add CORS middleware for cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # Điền biến origins vừa tạo ở trên vào đây
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Welcome to ProjectFile API"}


@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
