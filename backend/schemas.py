from pydantic import BaseModel, ConfigDict
from datetime import datetime

class FileRecordResponse(BaseModel):
    id: int
    original_filename: str
    system_filename: str
    file_size_bytes: int
    uploaded_at: datetime

    model_config = ConfigDict(from_attributes=True)