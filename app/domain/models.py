from dataclasses import dataclass, field
from datetime import datetime
import uuid

@dataclass
class Message:
    room_id: str
    sender: str
    content: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = field(default_factory=datetime.utcnow)