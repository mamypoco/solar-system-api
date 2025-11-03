def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_all_planets_with_one_record(client, one_planet):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [
        {
        "id": 1,
        "name": "Venus",
        "description": "green and wet",
        "size": "large"
    }
    ]

def test_get_one_planet_succeeds(client, one_planet):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Venus",
        "description": "green and wet",
        "size": "large"
    }

def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "Pluto",
        "description": "really far away and not in solar system",
        "size": "large"

    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "Pluto",
        "description": "really far away and not in solar system",
        "size": "large" }
    
def test_create_one_planet_no_description(client):
    # Arrange
    test_data = {"size": "large",
                 "name": "Venus"}

    # Act
    response = client.post("/planets", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {'message': 'Invalid request: missing description'}


def test_create_one_planet_with_extra_keys(client):
    # Arrange
    test_data = {
        "name": "Earth",
        "size": "medium",
        "description": "A New Planet on Board!",
        "another": "last value"
    }

    # Act
    response = client.post("/planets", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "Earth",
        "size": "medium",
        "description": "A New Planet on Board!"
    }
