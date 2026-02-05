def test_create_message(client):
    chat = client.post("/chats", json={"title": "Chat"}).json()

    response = client.post(
        f"/chats/{chat['id']}/messages",
        json={"text": "hello"},
    )
    assert response.status_code == 201

    payload = response.json()
    assert payload["chat_id"] == chat["id"]
    assert payload["text"] == "hello"


def test_create_message_empty_text(client):
    chat = client.post("/chats", json={"title": "Chat"}).json()
    response = client.post(
        f"/chats/{chat['id']}/messages",
        json={"text": ""},
    )
    assert response.status_code == 422


def test_create_message_spaces_only_text(client):
    chat = client.post("/chats", json={"title": "Chat"}).json()
    response = client.post(
        f"/chats/{chat['id']}/messages",
        json={"text": "   "},
    )
    assert response.status_code == 422


def test_create_message_for_missing_chat(client):
    response = client.post("/chats/999/messages", json={"text": "hello"})
    assert response.status_code == 404


def test_delete_chat_cascade(client):
    chat = client.post("/chats", json={"title": "Chat"}).json()

    client.post(
        f"/chats/{chat['id']}/messages",
        json={"text": "msg"},
    )

    client.delete(f"/chats/{chat['id']}")

    response = client.get(f"/chats/{chat['id']}")
    assert response.status_code == 404
