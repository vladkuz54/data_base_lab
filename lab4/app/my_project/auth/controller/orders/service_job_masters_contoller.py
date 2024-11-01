from typing import List

from lab4.app.my_project.auth.service import service_job_masters_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class ServiceJobMastersController(GeneralController):

    _service = service_job_masters_service

    def get_masters_after_service_jobs(self, service_job_id: int) -> List[object]:
        return self._service.get_masters_after_service_jobs(service_job_id)

    def get_service_job_after_masters(self, master_id: int) -> List[object]:
        return self._service.get_service_job_after_masters(master_id)
