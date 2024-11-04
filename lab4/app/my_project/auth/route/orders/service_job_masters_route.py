from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import service_job_masters_controller
from lab4.app.my_project.auth.domain import ServiceJobMasters

service_job_masters_bp = Blueprint('service_job_masters', __name__, url_prefix='/service_job_masters')


@service_job_masters_bp.get('')
def get_all_service_job_masters() -> Response:
    return make_response(jsonify(service_job_masters_controller.find_all()), HTTPStatus.OK)


@service_job_masters_bp.post('')
def create_service_job_master() -> Response:
    content = request.get_json()
    service_job_masters = ServiceJobMasters.create_from_dto(content)
    service_job_masters_controller.create(service_job_masters)
    return make_response(jsonify(service_job_masters.put_into_dto()), HTTPStatus.CREATED)


@service_job_masters_bp.get('/<int:service_job_masters_id>')
def get_service_job_master(service_job_masters_id: int) -> Response:
    return make_response(jsonify(service_job_masters_controller.find_by_id(service_job_masters_id)), HTTPStatus.OK)


@service_job_masters_bp.put('/<int:service_job_masters_id>')
def update_service_job_master(service_job_masters_id: int) -> Response:
    content = request.get_json()
    service_job_masters = ServiceJobMasters.create_from_dto(content)
    service_job_masters_controller.update(service_job_masters_id, service_job_masters)
    return make_response("Service type updated", HTTPStatus.OK)


@service_job_masters_bp.patch('/<int:service_job_masters_id>')
def patch_service_job_master(service_job_masters_id: int) -> Response:
    content = request.get_json()
    service_job_masters_controller.patch(service_job_masters_id, content)
    return make_response("Service type updated", HTTPStatus.OK)


@service_job_masters_bp.delete('/<int:service_job_masters_id>')
def delete_service_job_master(service_job_masters_id: int) -> Response:
    service_job_masters_controller.delete(service_job_masters_id)
    return make_response("Service type deleted", HTTPStatus.OK)


@service_job_masters_bp.get('/get-masters-after-service-job/<int:service_job_id>')
def get_masters_after_service_jobs(service_job_id: int) -> Response:
    return make_response(jsonify(service_job_masters_controller.get_masters_after_service_jobs(service_job_id)),
                         HTTPStatus.OK)


@service_job_masters_bp.get('/get-service-jobs-after-master/<int:master_id>')
def get_service_job_after_masters(master_id: int) -> Response:
    return make_response(jsonify(service_job_masters_controller.get_service_job_after_masters(master_id)),
                         HTTPStatus.OK)
