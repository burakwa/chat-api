from app.repositories.base import ChatRepository
from app.domain.models import Message
from typing import List

class ChatService:
    def __init__(self, chat_repository: ChatRepository):
        self.chat_repository = chat_repository

    def send_message(self, room_id: str, sender: str, content: str) -> Message:
        # Buraya ileride spam koruması, küfür filtresi gibi business logic'ler eklenebilir.
        message = Message(room_id=room_id, sender=sender, content=content)
        self._repository.save_message(message)
        return message

    def get_room_history(self, room_id: str) -> List[Message]:
        return self._repository.get_messages(room_id)