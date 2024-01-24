import random

def test_create_avm(client_with_auth):
    response = client_with_auth.post('/avm-data', json=[
        {
            "address": "Address " + str(random.randint(1, 100)),
            "latitude": random.uniform(-90, 90),
            "longitude": random.uniform(-180, 180),
            "zipcode": str(random.randint(10000, 99999)),
            "city": "Barcelona",
            "year_of_construction": random.randint(1900, 2022),
            "year_of_renovation": random.randint(1900, 2022),
            "total_price": random.randint(100000, 1000000),
            "total_area": random.randint(50, 200),
            "price_m2": 4390,
            "has_elevator": random.choice([True, False]),
            "valuation_date": str(random.randint(1, 31)) + "/09/2021"
        },
        {
            "address": "Address " + str(random.randint(1, 100)),
            "latitude": random.uniform(-90, 90),
            "longitude": random.uniform(-180, 180),
            "zipcode": "123098",
            "city": "Valencia",
            "year_of_construction": random.randint(1900, 2022),
            "year_of_renovation": random.randint(1900, 2022),
            "total_price": random.randint(100000, 1000000),
            "total_area": random.randint(50, 200),
            "price_m2": 3500,
            "has_elevator": random.choice([True, False]),
            "valuation_date": str(random.randint(1, 31)) + "/09/2021"
        },
        {
            "address": "Address " + str(random.randint(1, 100)),
            "latitude": random.uniform(-90, 90),
            "longitude": random.uniform(-180, 180),
            "zipcode": str(random.randint(10000, 99999)),
            "city": "Barcelona",
            "year_of_construction": random.randint(1900, 2022),
            "year_of_renovation": random.randint(1900, 2022),
            "total_price": random.randint(100000, 1000000),
            "total_area": random.randint(50, 200),
            "price_m2": 5421,
            "has_elevator": random.choice([True, False]),
            "valuation_date": str(random.randint(1, 31)) + "/09/2021"
        },
        {
            "address": "Address " + str(random.randint(1, 100)),
            "latitude": random.uniform(-90, 90),
            "longitude": random.uniform(-180, 180),
            "zipcode": "123098",
            "city": "Valencia",
            "year_of_construction": random.randint(1900, 2022),
            "year_of_renovation": random.randint(1900, 2022),
            "total_price": random.randint(100000, 1000000),
            "total_area": random.randint(50, 200),
            "price_m2": 3280,
            "has_elevator": random.choice([True, False]),
            "valuation_date": str(random.randint(1, 31)) + "/09/2021"
        },
    ])

    assert response.status_code == 200


def test_create_avm_error_field_required(client_with_auth):
    response = client_with_auth.post('/avm-data', json=[
        {
            "latitude": 41.410610,
            "longitude": 2.161880,
            "zipcode": "08025",
            "city": "Barcelona",
            "year_of_construction": 1900,
            "year_of_renovation": 2020,
            "total_price": 450000,
            "total_area": 83,
            "price_m2": 5421,
            "has_elevator": True,
            "valuation_date": "10/09/2021"
        }
    ])

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "missing",
                "loc": [
                    "body",
                    0,
                    "address",
                ],
                "msg": "Field required",
                "input": {
                    "latitude": 41.41061,
                    "longitude": 2.16188,
                    "zipcode": "08025",
                    "city": "Barcelona",
                    "year_of_construction": 1900,
                    "year_of_renovation": 2020,
                    "total_price": 450000,
                    "total_area": 83,
                    "price_m2": 5421,
                    "has_elevator": True,
                    "valuation_date": "10/09/2021"
                },
                "url": "https://errors.pydantic.dev/2.5/v/missing"
            }
        ]
    }
