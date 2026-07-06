from app.repositories.base import ChatRepository
from app.domain.models import Message
from typing import List, Dict

class InMemoryChatRepository(ChatRepository):
    def __init__(self):
        # Şimdilik veriyi RAM'de tutuyoruz.
        self._db: Dict[str, List[Message]] = {}

    def save_message(self, message: Message) -> None:
        if message.room_id not in self._db:
            self._db[message.room_id] = []
        self._db[message.room_id].append(message)

    def get_messages(self, room_id: str) -> List[Message]:
        return self._db.get(room_id, [])