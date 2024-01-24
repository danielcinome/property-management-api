import pytest


@pytest.mark.usefixtures("test_create_avm")
def test_get_average_price_per_square_meter_by_city(client):
    response = client.get('/property/average-price/city/Barcelona')
    assert response.status_code == 200
    assert response.json() == {'average_price_per_square_meter': 4905.5}


@pytest.mark.usefixtures("test_create_avm")
def test_get_average_price_per_square_meter_by_area(client):
    response = client.get('/property/average-price/zipcode/123098')
    assert response.status_code == 200
    assert response.json() == {'average_price_per_square_meter': 3390.0}


def test_get_average_price_per_square_meter_by_city_not_found(client):
    response = client.get('/property/average-price/city/Barcelona_wrong')
    assert response.status_code == 404
    assert response.json() == {
        'detail': 'Error calculating average price: No city found for the specified name'}


def test_get_average_price_per_square_meter_by_area_not_found(client):
    response = client.get('/property/average-price/zipcode/123098_wrong')
    assert response.status_code == 404
    assert response.json() == {
        'detail': 'Error calculating average price: No properties found for the specified area city'}


def test_get_average_price_per_square_meter_by_type_not_found(client):
    response = client.get('/property/average-price/zipcode_wrong/123098')
    assert response.status_code == 422
    assert response.json() == {'detail': [{'type': 'enum', 'loc': [
        'path', 'area_type'], 'msg': "Input should be 'city' or 'zipcode'", 'input': 'zipcode_wrong', 'ctx': {'expected': "'city' or 'zipcode'"}}]}
