from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import masters_controller
from lab4.app.my_project.auth.domain import Masters

masters_bp = Blueprint('masters', __name__, url_prefix='/masters')


@masters_bp.get('')
def get_all_masters() -> Response:
    return make_response(jsonify(masters_controller.find_all()), HTTPStatus.OK)


@masters_bp.post('')
def create_master() -> Response:
    content = request.get_json()
    masters = Masters.create_from_dto(content)
    masters_controller.create(masters)
    return make_response(jsonify(masters.put_into_dto()), HTTPStatus.CREATED)


@masters_bp.get('/<int:master_id>')
def get_master(master_id: int) -> Response:
    return make_response(jsonify(masters_controller.find_by_id(master_id)), HTTPStatus.OK)


@masters_bp.put('/<int:master_id>')
def update_master(master_id: int) -> Response:
    content = request.get_json()
    masters = Masters.create_from_dto(content)
    masters_controller.update(master_id, masters)
    return make_response("Master updated", HTTPStatus.OK)


@masters_bp.patch('/<int:master_id>')
def patch_master(master_id: int) -> Response:
    content = request.get_json()
    masters_controller.patch(master_id, content)
    return make_response("Master updated", HTTPStatus.OK)


@masters_bp.delete('/<int:master_id>')
def delete_master(master_id: int) -> Response:
    masters_controller.delete(master_id)
    return make_response("Master deleted", HTTPStatus.OK)