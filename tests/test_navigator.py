import pytest
from nav.db import get_db

def test_index(client):
    response = client.get('/')
    assert b"Add" in response.data
    assert b"Edit" in response.data
    assert b"Delete" in response.data


def test_add(client,app):
    response = client.post('/')
    client.post('/', data={'maincategory': 'IBM', 'subcategory': 'Power', 'urlname': 'E980', 'urllocation': 'e980.com'})
    with app.app_context():
        db = get_db()
        link = db.execute('SELECT * FROM links WHERE id = 2').fetchone()
        assert link['maincategory'] == 'IBM'

def test_edit(client,app):
    response = client.post('/1')
    client.post('/1', data={'maincategory': 'test', 'subcategory': 'ebook', 'urlname': 'big1000', 'urllocation': 'ebook.big1000.com'})
    with app.app_context():
        db = get_db()
        link = db.execute('SELECT * FROM links WHERE id = 1').fetchone()
        assert link['maincategory'] == 'test'

def test_delete(client,app):
    response = client.post('/1/delete')
    assert response.headers['Location'] == 'http://localhost/'
    with app.app_context():
        db = get_db()
        link = db.execute('SELECT * FROM links WHERE id = 1').fetchone()
        assert link is None
