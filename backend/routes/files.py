from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models import FileRecord
from backend.schemas import FileRecordResponse

router = APIRouter(prefix="/files", tags=["Files"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[FileRecordResponse])
def get_files(db: Session = Depends(get_db)):
    return db.query(FileRecord).all()
