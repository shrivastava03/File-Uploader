import sys
sys.path.append('.')  # Add current directory to path

from backend.database import SessionLocal
from backend.models import FileRecord

db = SessionLocal()
files = db.query(FileRecord).all()
print(f"Total files in database: {len(files)}")
for file in files:
    print(f"- {file.original_filename} ({file.file_size_bytes} bytes) - Uploaded: {file.uploaded_at}")
db.close()