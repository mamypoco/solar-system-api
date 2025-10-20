from flask import Blueprint, make_response, abort
from app.models.planets import planets

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.get("")
def get_all_planets():
    results_list = []

    for planet in planets:
        results_list.append(dict(
            id = planet.id,
            name = planet.name,
            description = planet.description,
            size = planet.size        
        ))

    return results_list

@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "size": planet.size
    }

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        response = {"message": f"Planet {planet_id} is invalid."}
        abort(make_response(response, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet

    response = {"message": f"Planet ID {planet_id} not found."}
    abort(make_response(response, 404))




 
        