"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200

def test_request_about(client):
    """This makes the about page"""
    response = client.get("/about")
    assert response.status_code == 200

def test_request_page_not_found(client):
    """This checks for a non-hosted page"""
    response = client.get("/page5")
    assert response.status_code == 404