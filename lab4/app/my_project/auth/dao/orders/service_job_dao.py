from typing import List, Dict, Any

import sqlalchemy

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import ServiceJob


class ServiceJobDAO(GeneralDAO):
    _domain_type = ServiceJob

    def get_service_jobs_after_service_type(self, service_type_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_service_jobs_after_service_type(:p1)"),
                                       {'p1': service_type_id}).mappings().all()
        return [dict(row) for row in result]

    def get_service_jobs_after_terminal(self, terminal_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_service_jobs_after_terminal(:p1)"),
                                       {'p1': terminal_id}).mappings().all()
        return [dict(row) for row in result]
