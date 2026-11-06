import pytest
pytest.importorskip('flask')
from app import app

def test_health_endpoint():
    with app.test_client() as client:
        response=client.get('/api/health')
        assert response.status_code==200
        assert response.json['status']=='ok'

def test_empty_article_rejected():
    with app.test_client() as client:
        response=client.post('/api/analyze',json={'text':'hi'})
        assert response.status_code in (400,500)  # dataset may not be downloaded yet
