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