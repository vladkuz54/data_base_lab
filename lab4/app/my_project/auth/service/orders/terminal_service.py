from typing import List

from lab4.app.my_project.auth.dao import terminal_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class TerminalService(GeneralService):

    _dao = terminal_dao

    def get_terminals_after_shop(self, shop_id: int) -> List[object]:
        return self._dao.get_terminals_after_shop(shop_id)

    def get_terminals_after_manufacturer(self, manufactures_id) -> List[object]:
        return self._dao.get_terminals_after_manufacturer(manufactures_id)
