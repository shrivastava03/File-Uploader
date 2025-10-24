from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import upload, files

app = FastAPI(title="File Uploader and Tracker")

# Allow frontend access (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(upload.router)
app.include_router(files.router)

@app.get("/")
def root():
    return {"message": "Welcome to the File Uploader API"}
