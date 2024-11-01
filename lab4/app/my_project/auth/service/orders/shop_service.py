from typing import List, Dict, Any

from lab4.app.my_project.auth.dao import shop_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class ShopService(GeneralService):

    _dao = shop_dao

    def get_shops_after_client(self, client_id: int) -> List[object]:
        return self._dao.get_shops_after_client(client_id)

