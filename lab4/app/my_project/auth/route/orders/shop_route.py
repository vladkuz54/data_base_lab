from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import shop_controller
from lab4.app.my_project.auth.domain import Shop

shop_bp = Blueprint('shops', __name__, url_prefix='/shops')


@shop_bp.get('')
def get_all_shops() -> Response:
    return make_response(jsonify(shop_controller.find_all()), HTTPStatus.OK)


@shop_bp.post('')
def create_shop() -> Response:
    content = request.get_json()
    shop = Shop.create_from_dto(content)
    shop_controller.create(shop)
    return make_response(jsonify(shop.put_into_dto()), HTTPStatus.CREATED)


@shop_bp.get('/<int:shop_id>')
def get_shop(shop_id: int) -> Response:
    return make_response(jsonify(shop_controller.find_by_id(shop_id)), HTTPStatus.OK)


@shop_bp.put('/<int:shop_id>')
def update_shop(shop_id: int) -> Response:
    content = request.get_json()
    shop = Shop.create_from_dto(content)
    shop_controller.update(shop_id, shop)
    return make_response("Shop updated", HTTPStatus.OK)


@shop_bp.patch('/<int:shop_id>')
def patch_shop(shop_id: int) -> Response:
    content = request.get_json()
    shop_controller.patch(shop_id, content)
    return make_response("Shop updated", HTTPStatus.OK)


@shop_bp.delete('/<int:shop_id>')
def delete_shop(shop_id: int) -> Response:
    shop_controller.delete(shop_id)
    return make_response("Shop deleted", HTTPStatus.OK)


@shop_bp.get('/get-shops-after-client/<int:client_id>')
def get_shops_after_client(client_id: int) -> Response:
    return make_response(jsonify(shop_controller.get_shops_after_client(client_id)), HTTPStatus.OK)
