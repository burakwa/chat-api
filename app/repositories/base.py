from abc import ABC, abstractmethod
from app.domain.models import Message
from typing import List

class ChatRepository(ABC):
    """
    Bu bir arayüzdür (Interface). 
    Yarın Redis veya PostgreSQL kullanacaksan sadece bu arayüzü implemente eden 
    yeni bir class yazman yeterli. Business logic'e dokunmana gerek kalmaz.
    """
    @abstractmethod
    def save_message(self, message: Message) -> None:
        pass

    @abstractmethod
    def get_messages(self, room_id: str) -> List[Message]:
        pass