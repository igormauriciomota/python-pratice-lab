def test_home_returns_success(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "dados em decisões" in response.get_data(as_text=True)


def test_admin_redirects_anonymous_user(client):
    response = client.get("/admin/", follow_redirects=False)
    assert response.status_code == 302
    assert "/auth/login" in response.headers["Location"]
