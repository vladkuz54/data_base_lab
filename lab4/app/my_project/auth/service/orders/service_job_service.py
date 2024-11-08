from typing import List

from lab4.app.my_project.auth.dao import service_job_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class ServiceJobService(GeneralService):

    _dao = service_job_dao

    def get_service_jobs_after_service_type(self, service_type_id: int) -> List[object]:
        return self._dao.get_service_jobs_after_service_type(service_type_id)

    def get_service_jobs_after_terminal(self, terminal_id: int) -> List[object]:
        return self._dao.get_service_jobs_after_terminal(terminal_id)
