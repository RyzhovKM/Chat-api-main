def test_create_chat(client):
    response = client.post("/chats", json={"title": "Test chat"})
    assert response.status_code == 201

    data = response.json()
    assert data["title"] == "Test chat"
    assert "id" in data


def test_create_chat_empty_title(client):
    response = client.post("/chats", json={"title": ""})
    assert response.status_code == 422


def test_create_chat_only_spaces_title(client):
    response = client.post("/chats", json={"title": "    "})
    assert response.status_code == 422


def test_get_chat_with_messages_order_and_limit(client):
    chat = client.post("/chats", json={"title": "Chat"}).json()

    client.post(f"/chats/{chat['id']}/messages", json={"text": "first"})
    client.post(f"/chats/{chat['id']}/messages", json={"text": "second"})
    client.post(f"/chats/{chat['id']}/messages", json={"text": "third"})

    response = client.get(f"/chats/{chat['id']}?limit=2")
    assert response.status_code == 200

    payload = response.json()
    assert payload["chat"]["id"] == chat["id"]
    assert [message["text"] for message in payload["messages"]] == ["second", "third"]


def test_get_chat_with_invalid_limit(client):
    chat = client.post("/chats", json={"title": "Chat"}).json()
    response = client.get(f"/chats/{chat['id']}?limit=0")
    assert response.status_code == 200
