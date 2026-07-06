from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class MessageCreate(BaseModel):
    room_id: str = Field(..., description="Mesajın gönderileceği oda ID'si")
    sender: str = Field(..., min_length=3, max_length=50)
    content: str = Field(..., min_length=1, max_length=1000)

class MessageResponse(BaseModel):
    id: str
    room_id: str
    sender: str
    content: str
    timestamp: datetime

    class Config:
        from_attributes = True
