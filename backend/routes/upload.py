import os
import uuid
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import SessionLocal, engine, Base
from backend.models import FileRecord

Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/upload-document", tags=["Upload"])

UPLOAD_DIR = "backend/uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
async def upload_document(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        system_filename = f"{uuid.uuid4()}_{file.filename}"
        file_path = os.path.join(UPLOAD_DIR, system_filename)

        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        file_size = os.path.getsize(file_path)

        db_record = FileRecord(
            original_filename=file.filename,
            system_filename=system_filename,
            file_size_bytes=file_size,
        )
        db.add(db_record)
        db.commit()
        db.refresh(db_record)

        return {"message": "File uploaded successfully!", "file_id": db_record.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
