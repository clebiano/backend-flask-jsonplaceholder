def test_get_n_todos_should_work(test_app):
    # GIVEN
    client = test_app.test_client()

    # WHEN
    resp = client.get("/todos?size=5", headers={"Authorization": "Bearer secret-token-test-1"})
    items = resp.json.get("items")

    # THEN
    assert resp.status_code == 200
    assert isinstance(items, list)
    assert len(items) == 5
    assert "id" in items[0].keys()
    assert "title" in items[0].keys()
