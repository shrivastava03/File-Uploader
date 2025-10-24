from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from backend.database import Base

class FileRecord(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    original_filename = Column(String, nullable=False)
    system_filename = Column(String, unique=True, nullable=False)
    file_size_bytes = Column(Integer, nullable=False)
    uploaded_at = Column(DateTime, default=datetime.utcnow)
