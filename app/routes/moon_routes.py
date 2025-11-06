from .routes_utilities import validate_model, create_model, get_models_with_filters
from flask import Blueprint, request, Response
from ..models.moon import Moon
from ..db import db

bp = Blueprint("moon_bp", __name__, url_prefix="/moons")

@bp.post("")
def create_moon():
    request_body = request.get_json()
    
    return create_model(Moon, request_body)

@bp.get("")
def get_all_moons():
    return get_models_with_filters(Moon, request.args)

@bp.get("/<id>")
def get_single_moon(id):
    moon = validate_model(Moon, id)

    return moon.to_dict()

@bp.put("/<id>")
def replace_moon(id):
    moon = validate_model(Moon, id)

    request_body = request.get_json()
    moon.name = request_body["name"]
    moon.description = request_body["description"]

    db.session.commit()

    return Response(status=204, mimetype="application/json")

@bp.delete("/<id>")
def delete_moon(id):
    moon = validate_model(Moon, id)

    db.session.delete(moon)
    db.session.commit()

    return Response(status=204, mimetype="application/json")