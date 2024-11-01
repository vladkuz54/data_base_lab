from typing import List

from lab4.app.my_project.auth.service import terminals_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class TerminalController(GeneralController):
    _service = terminals_service

    def get_terminals_after_shop(self, shop_id) -> List[object]:
        return self._service.get_terminals_after_shop(shop_id)

    def get_terminals_after_manufacturer(self, manufactures_id) -> List[object]:
        return self._service.get_terminals_after_manufacturer(manufactures_id)
