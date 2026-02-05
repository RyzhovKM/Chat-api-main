def test_create_chat(client):
    response = client.post("/chats", json={"title": "Test chat"})
    assert response.status_code == 201

    data = response.json()
    assert data["title"] == "Test chat"
    assert "id" in data

def test_create_chat_empty_title(client):
    response = client.post("/chats", json={"title": ""})
    assert response.status_code == 422
