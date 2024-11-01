from typing import List, Dict, Any

import sqlalchemy

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import ServiceJobMasters


class ServiceJobMastersDAO(GeneralDAO):
    _domain_type = ServiceJobMasters

    def get_masters_after_service_jobs(self, service_job_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_masters_after_service_jobs(:p1)"),
                                     {"p1": service_job_id}).mappings().all()
        return [dict(row) for row in result]

    def get_service_job_after_masters(self, master_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_service_job_after_masters(:p1)"),
                                       {'p1': master_id}).mappings().all()
        return [dict(row) for row in result]
