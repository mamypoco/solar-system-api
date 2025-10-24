from flask import Blueprint, make_response, abort, request
from app.models.planets import Planet
from ..db import db

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    name = request_body["name"]
    description = request_body["description"]
    size = request_body["size"]

    new_planet = Planet(
        name=name,
        description=description,
        size=size
    )
    db.session.add(new_planet)
    db.session.commit()

    planet_response = dict(
        id=new_planet.id,
        name=new_planet.name,
        description=new_planet.description,
        size=new_planet.size
    )

    return planet_response, 201

@planets_bp.get("")
def get_all_planets():
    query = db.select(Planet).order_by(Planet.id)
    planets = db.session.scalars(query)
    result_list = []

    for planet in planets:
        result_list.append(dict(
            id=planet.id,
            name=planet.name,
            description=planet.description,
            size=planet.size
        ))

    return result_list