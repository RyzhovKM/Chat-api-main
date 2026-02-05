def test_delete_chat_cascade(client):
    chat = client.post("/chats", json={"title": "Chat"}).json()

    client.post(
        f"/chats/{chat['id']}/messages",
        json={"text": "msg"}
    )

    client.delete(f"/chats/{chat['id']}")

    response = client.get(f"/chats/{chat['id']}")
    assert response.status_code == 404
