from typing import List

from lab4.app.my_project.auth.dao import service_job_masters_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class ServiceJobMastersService(GeneralService):

    _dao = service_job_masters_dao

    def get_masters_after_service_jobs(self, service_job_id: int) -> List[object]:
        return self._dao.get_masters_after_service_jobs(service_job_id)

    def get_service_job_after_masters(self, master_id: int) -> List[object]:
        return self._dao.get_service_job_after_masters(master_id)
