from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import service_job_controller
from lab4.app.my_project.auth.domain import ServiceJob

service_job_bp = Blueprint('service_jobs', __name__, url_prefix='/service_jobs')


@service_job_bp.get('')
def get_all_service_jobs() -> Response:
    return make_response(jsonify(service_job_controller.find_all()), HTTPStatus.OK)


@service_job_bp.post('')
def create_service_job() -> Response:
    content = request.get_json()
    service_job = ServiceJob.create_from_dto(content)
    service_job_controller.create(service_job)
    return make_response(jsonify(service_job.put_into_dto()), HTTPStatus.CREATED)


@service_job_bp.get('/<int:service_job_id>')
def get_service_job(service_job_id: int) -> Response:
    return make_response(jsonify(service_job_controller.find_by_id(service_job_id)), HTTPStatus.OK)


@service_job_bp.put('/<int:service_job_id>')
def update_service_job(service_job_id: int) -> Response:
    content = request.get_json()
    service_job = ServiceJob.create_from_dto(content)
    service_job_controller.update(service_job_id, service_job)
    return make_response("Service type updated", HTTPStatus.OK)


@service_job_bp.patch('/<int:service_job_id>')
def patch_service_job(service_job_id: int) -> Response:
    content = request.get_json()
    service_job_controller.patch(service_job_id, content)
    return make_response("Service type updated", HTTPStatus.OK)


@service_job_bp.delete('/<int:service_job_id>')
def delete_service_job(service_job_id: int) -> Response:
    service_job_controller.delete(service_job_id)
    return make_response("Service type deleted", HTTPStatus.OK)


@service_job_bp.get('/get_service_jobs_after_service_type/<int:service_type_id>')
def get_service_jobs_after_service_type(service_type_id: int) -> Response:
    return make_response(jsonify(service_job_controller.get_service_jobs_after_service_type(service_type_id)),
                         HTTPStatus.OK)
