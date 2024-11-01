from typing import List

from lab4.app.my_project.auth.dao import client_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class ClientService(GeneralService):

    _dao = client_dao

    def get_clients_name_filter(self, name_filter: str) -> List[object]:
        return self._dao.get_clients_name_filter(name_filter)
