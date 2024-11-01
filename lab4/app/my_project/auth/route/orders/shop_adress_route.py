from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import shop_adress_controller
from lab4.app.my_project.auth.domain import Shop_Adress

shop_adress_bp = Blueprint('shop_adresses', __name__, url_prefix='/shop_adresses')


@shop_adress_bp.get('')
def get_all_shop_adresses() -> Response:
    return make_response(jsonify(shop_adress_controller.find_all()), HTTPStatus.OK)


@shop_adress_bp.post('')
def create_shop_adress() -> Response:
    content = request.get_json()
    shop_adress = Shop_Adress.create_from_dto(content)
    shop_adress_controller.create(shop_adress)
    return make_response(jsonify(shop_adress.put_into_dto()), HTTPStatus.CREATED)


@shop_adress_bp.get('/<int:shop_adress_id>')
def get_shop_adress(shop_adress_id: int) -> Response:
    return make_response(jsonify(shop_adress_controller.find_by_id(shop_adress_id)), HTTPStatus.OK)


@shop_adress_bp.put('/<int:shop_adress_id>')
def update_shop_adress(shop_adress_id: int) -> Response:
    content = request.get_json()
    shop_adress = Shop_Adress.create_from_dto(content)
    shop_adress_controller.update(shop_adress_id, shop_adress)
    return make_response("Shop adress was updated", HTTPStatus.OK)


@shop_adress_bp.patch('/<int:shop_adress_id>')
def patch_shop_adress(shop_adress_id: int) -> Response:
    content = request.get_json()
    shop_adress_controller.patch(shop_adress_id, content)
    return make_response("Shop adress was updated", HTTPStatus.OK)


@shop_adress_bp.delete('/<int:shop_adress_id>')
def delete_shop_adress(shop_adress_id: int) -> Response:
    shop_adress_controller.delete(shop_adress_id)
    return make_response("Shop adress was deleted", HTTPStatus.OK)


@shop_adress_bp.get('/get-shop_adress-after-number/<int:in_num>')
def get_shop_adress_after_number(in_num: int) -> Response:
    return make_response(jsonify(shop_adress_controller.get_shop_adress_after_number(in_num)), HTTPStatus.OK)

