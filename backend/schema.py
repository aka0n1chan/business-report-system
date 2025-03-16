from pydantic import BaseModel
from datetime import datetime

class ReportCreate(BaseModel):
    title: str
    content: str

class ReportResponse(BaseModel):
    id: int
    title: str
    content: str
    progress: str
    created_at: datetime

    class Config:
        orm_mode = True
