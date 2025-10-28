from flask import Blueprint, make_response, abort, request, Response
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


@planets_bp.get("/<id>")
def get_single_planet():
    planet = validate_planet(id)
    planet_dict = dict(
            id=planet.id,
            name=planet.name,
            description=planet.description,
            size=planet.size
        )

    return planet_dict

def validate_planet(id):
    try:
        id = int(id)
    except ValueError:
        invalid = {"message": f"Planet id ({id}) is invalid."}
        abort(make_response(invalid, 400))
        
    query = db.select(Planet).where(Planet.id == id)
    planet = db.session.scalar(query)
    if not planet:
        not_found = {"message": f"Planet with id ({id}) not found"}
        abort(make_response(not_found, 404))
    return planet


@planets_bp.put("/<id>")
def replace_planet(id):
    planet = validate_planet(id)
    request_body = request.get_json()
    
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.size = request_body["size"]
    db.session.commit()

    return Response(status=204, mimetype="application/json")



@planets_bp.delete("/<id>")
def delete_planet(id):
    planet = validate_planet(id)
    
    db.session.delete(planet)
    db.session.commit()
    
    return Response(status=204, mimetype="application/json")