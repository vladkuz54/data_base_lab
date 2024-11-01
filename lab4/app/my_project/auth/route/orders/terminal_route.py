from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import terminal_controller
from lab4.app.my_project.auth.domain import Terminal

terminal_bp = Blueprint('terminals', __name__, url_prefix='/terminals')


@terminal_bp.get('')
def get_all_terminals() -> Response:
    return make_response(jsonify(terminal_controller.find_all()), HTTPStatus.OK)


@terminal_bp.post('')
def create_terminal() -> Response:
    content = request.get_json()
    terminal = Terminal.create_from_dto(content)
    terminal_controller.create(terminal)
    return make_response(jsonify(terminal.put_into_dto()), HTTPStatus.CREATED)


@terminal_bp.get('/<int:terminal_id>')
def get_terminal(terminal_id: int) -> Response:
    return make_response(jsonify(terminal_controller.find_by_id(terminal_id)), HTTPStatus.OK)


@terminal_bp.put('/<int:terminal_id>')
def update_terminal(terminal_id: int) -> Response:
    content = request.get_json()
    terminal = Terminal.create_from_dto(content)
    terminal_controller.update(terminal_id, terminal)
    return make_response("Terminal updated", HTTPStatus.OK)


@terminal_bp.patch('/<int:terminal_id>')
def patch_terminal(terminal_id: int) -> Response:
    content = request.get_json()
    terminal_controller.patch(terminal_id, content)
    return make_response("Terminal updated", HTTPStatus.OK)


@terminal_bp.delete('/<int:terminal_id>')
def delete_terminal(terminal_id: int) -> Response:
    terminal_controller.delete(terminal_id)
    return make_response("Terminal deleted", HTTPStatus.OK)


@terminal_bp.get('/get_terminals_after_shop/<int:shop_id>')
def get_terminals_after_shop(shop_id: int) -> Response:
    return make_response(jsonify(terminal_controller.get_terminals_after_shop(shop_id)),
                         HTTPStatus.OK)


@terminal_bp.get('/get_terminals_after_manufacturer/<int:manufactures_id>')
def get_terminals_after_manufacturer(manufactures_id: int) -> Response:
    return make_response(jsonify(terminal_controller.get_terminals_after_manufacturer(manufactures_id)),
                         HTTPStatus.OK)

