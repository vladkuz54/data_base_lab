from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import invoices_controller
from lab4.app.my_project.auth.domain import Invoices

invoices_bp = Blueprint('invoices', __name__, url_prefix='/invoices')


@invoices_bp.get('')
def get_all_clients() -> Response:
    return make_response(jsonify(invoices_controller.find_all()), HTTPStatus.OK)


@invoices_bp.post('')
def create_client() -> Response:
    content = request.get_json()
    invoices = Invoices.create_from_dto(content)
    invoices_controller.create(invoices)
    return make_response(jsonify(invoices.put_into_dto()), HTTPStatus.CREATED)


@invoices_bp.get('/<int:invoices_id>')
def get_client(invoices_id: int) -> Response:
    return make_response(jsonify(invoices_controller.find_by_id(invoices_id)), HTTPStatus.OK)


@invoices_bp.put('/<int:invoices_id>')
def update_client(invoices_id: int) -> Response:
    content = request.get_json()
    invoices = Invoices.create_from_dto(content)
    invoices_controller.update(invoices_id, invoices)
    return make_response("Invoice updated", HTTPStatus.OK)


@invoices_bp.patch('/<int:invoices_id>')
def patch_client(invoices_id: int) -> Response:
    content = request.get_json()
    invoices_controller.patch(invoices_id, content)
    return make_response("Invoice updated", HTTPStatus.OK)


@invoices_bp.delete('/<int:invoices_id>')
def delete_client(invoices_id: int) -> Response:
    invoices_controller.delete(invoices_id)
    return make_response("Invoice deleted", HTTPStatus.OK)


