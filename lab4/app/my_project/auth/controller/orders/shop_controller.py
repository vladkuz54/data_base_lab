from typing import List, Dict, Any

from lab4.app.my_project.auth.service import shop_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class ShopController(GeneralController):
    _service = shop_service

    def get_shops_after_client(self, client_id: int) -> List[object]:
        return self._service.get_shops_after_client(client_id)
