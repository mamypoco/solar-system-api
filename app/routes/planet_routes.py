from flask import Blueprint, request, Response, abort, make_response
from app.models.planets import Planet
from app.models.moon import Moon
from ..db import db
from .routes_utilities import validate_model, create_model

bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@bp.post("")
def create_planet():
    request_body = request.get_json()
    
    try: 
        new_planet = Planet.from_dict(request_body)

    except KeyError as error:
        response = {"message": f"Invalid request: missing {error.args[0]}"}
        abort(make_response(response, 400))    

    db.session.add(new_planet)
    db.session.commit()

    return new_planet.to_dict(), 201

# added in wave08
@bp.post("/<id>/moons")
def create_moons_with_planet_id(id):
    planet = validate_model(Planet, id)

    request_body = request.get_json()
    request_body["planet_id"] = planet.id

    return create_model(Moon, request_body)


@bp.get("/<id>/moons")
def get_all_planet_moons(id):
    planet = validate_model(Planet, id)
    moons = [moon.to_dict() for moon in planet.moons]

    return moons

# =============

@bp.get("")
def get_all_planets():
    query = db.select(Planet)
    name_param = request.args.get("name")
    size_param = request.args.get("size")
    description_param = request.args.get("description")

    if name_param:
        query = query.where(Planet.name == name_param)

    if size_param:
        query = query.where(Planet.size == size_param)

    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%"))

    query = query.order_by(Planet.id)

    planets = db.session.scalars(query)
    result_list = []

    for planet in planets:
        result_list.append(planet.to_dict())

    return result_list


@bp.get("/<id>")
def get_single_planet(id):
    planet = validate_model(Planet, id)

    return planet.to_dict()

@bp.put("/<id>")
def replace_planet(id):
    planet = validate_model(Planet, id)
    request_body = request.get_json()
    
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.size = request_body["size"]
    db.session.commit()

    return Response(status=204, mimetype="application/json")



@bp.delete("/<id>")
def delete_planet(id):
    planet = validate_model(Planet, id)
    
    db.session.delete(planet)
    db.session.commit()
    
    return Response(status=204, mimetype="application/json")


@bp.post("/<id>/cats")
def create_moon_with_planet_id(id):
    planet= validate_model(Planet, id)

    request_body = request.get_json()
    request_body["planet_id"] = planet.id

    return create_model(Moons, request_body)