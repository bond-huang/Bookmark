from nav import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_gump(client):
    response = client.get('/gump')
    assert response.data == b'Life was like a box of chocolates,you never know what you\'re gonna get.'
