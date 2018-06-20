from api.models import Client


def test_api_client_get(app, dbsession):
    client = Client(
        id=1,
        name='Mieszko',
        ip_address='1.1.1.1',
    )
    dbsession.add(client)
    response = app.get('/api/client')
    assert response.json() == {'num_results': 0, 'objects': [], 'page': 1, 'total_pages': 0}
