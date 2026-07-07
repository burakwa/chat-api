from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_send_and_get_messages():
    response = client.post(
        "/chat/messages",
        json={"room_id": "room-1", "sender": "alice", "content": "hello"},
    )

    assert response.status_code == 201
    payload = response.json()
    assert payload["room_id"] == "room-1"
    assert payload["sender"] == "alice"
    assert payload["content"] == "hello"

    history_response = client.get("/chat/rooms/room-1/messages")
    assert history_response.status_code == 200
    history = history_response.json()
    assert len(history) == 1
    assert history[0]["content"] == "hello"
