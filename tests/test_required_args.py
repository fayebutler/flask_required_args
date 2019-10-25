import pytest

from tests.test_app import app


@pytest.mark.parametrize("route, status_code, data", [
    ("/", 200, b'ok'),
    ("/?name=test", 200, b'ok'),
    ("/john", 200, b'john'),
    ("/john?name=test", 200, b'john'),
    ("/blah/john", 404, None)
])
def test_get_routes_no_data(route, status_code, data):
    with app.test_client() as c:
        response = c.get(route)
        print("RESPOSE ", response)
        print("data ", response.get_data())
        assert response.status_code == status_code
        if data:
            assert response.get_data() == data


@pytest.mark.parametrize("route, status_code, json, data", [
    ("/hello", 200, {}, b'Hello World'),
    ("/hello", 200, {'name': 'john'}, b'Hello john'),
    ("/hello/john", 200, {}, b'hello john'),
    ("/hello/john", 200, {'greeting': 'ciao'}, b'ciao john'),
])
def test_post_routes_data(route, status_code, json, data):
    with app.test_client() as c:
        response = c.post(route, json=json)
        print("RESPOSE ", response)
        print("data ", response.get_data())
        assert response.status_code == status_code
        if data:
            assert response.get_data() == data
