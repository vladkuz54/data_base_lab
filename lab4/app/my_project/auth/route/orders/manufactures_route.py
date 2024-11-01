from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import manufactures_controller
from lab4.app.my_project.auth.domain import Manufactures

manufactures_bp = Blueprint('manufactures', __name__, url_prefix='/manufactures')


@manufactures_bp.get('')
def get_all_manufactures() -> Response:
    return make_response(jsonify(manufactures_controller.find_all()), HTTPStatus.OK)


@manufactures_bp.post('')
def create_manufacture() -> Response:
    content = request.get_json()
    manufactures = Manufactures.create_from_dto(content)
    manufactures_controller.create(manufactures)
    return make_response(jsonify(manufactures.put_into_dto()), HTTPStatus.CREATED)


@manufactures_bp.get('/<int:manufacture_id>')
def get_manufacture(manufacture_id: int) -> Response:
    return make_response(jsonify(manufactures_controller.find_by_id(manufacture_id)), HTTPStatus.OK)


@manufactures_bp.put('/<int:manufacture_id>')
def update_manufacture(manufacture_id: int) -> Response:
    content = request.get_json()
    manufactures = Manufactures.create_from_dto(content)
    manufactures_controller.update(manufacture_id, manufactures)
    return make_response("Manufacture updated", HTTPStatus.OK)


@manufactures_bp.patch('/<int:manufacture_id>')
def patch_manufacture(manufacture_id: int) -> Response:
    content = request.get_json()
    manufactures_controller.patch(manufacture_id, content)
    return make_response("Manufacture updated", HTTPStatus.OK)


@manufactures_bp.delete('/<int:manufacture_id>')
def delete_manufacture(manufacture_id: int) -> Response:
    manufactures_controller.delete(manufacture_id)
    return make_response("Manufacture deleted", HTTPStatus.OK)