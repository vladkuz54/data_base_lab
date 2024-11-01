from typing import List

from lab4.app.my_project.auth.service import service_job_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class ServiceJobController(GeneralController):

    _service = service_job_service

    def get_service_jobs_after_service_type(self, service_type_id: int) -> List[object]:
        return self._service.get_service_jobs_after_service_type(service_type_id)
