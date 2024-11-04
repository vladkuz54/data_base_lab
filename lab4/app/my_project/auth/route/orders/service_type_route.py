from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import service_type_controller
from lab4.app.my_project.auth.domain import ServiceType

service_type_bp = Blueprint('service_types', __name__, url_prefix='/service-types')


@service_type_bp.get('')
def get_all_service_types() -> Response:
    return make_response(jsonify(service_type_controller.find_all()), HTTPStatus.OK)


@service_type_bp.post('')
def create_service_type() -> Response:
    content = request.get_json()
    service_type = ServiceType.create_from_dto(content)
    service_type_controller.create(service_type)
    return make_response(jsonify(service_type.put_into_dto()), HTTPStatus.CREATED)


@service_type_bp.get('/<int:service_type_id>')
def get_service_type(service_type_id: int) -> Response:
    return make_response(jsonify(service_type_controller.find_by_id(service_type_id)), HTTPStatus.OK)


@service_type_bp.put('/<int:service_type_id>')
def update_service_type(service_type_id: int) -> Response:
    content = request.get_json()
    service_type = ServiceType.create_from_dto(content)
    service_type_controller.update(service_type_id, service_type)
    return make_response("Service type updated", HTTPStatus.OK)


@service_type_bp.patch('/<int:service_type_id>')
def patch_service_type(service_type_id: int) -> Response:
    content = request.get_json()
    service_type_controller.patch(service_type_id, content)
    return make_response("Service type updated", HTTPStatus.OK)


@service_type_bp.delete('/<int:service_type_id>')
def delete_service_type(service_type_id: int) -> Response:
    service_type_controller.delete(service_type_id)
    return make_response("Service type deleted", HTTPStatus.OK)