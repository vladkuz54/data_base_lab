from typing import List

from lab4.app.my_project.auth.dao import shop_adress_dao
from lab4.app.my_project.auth.service.general_service import GeneralService

class ShopAdressService(GeneralService):

    _dao = shop_adress_dao

    def get_shop_adress_street_filter(self, street_name: str, street_number: str) -> List[object]:
        return self._dao.get_shop_adress_street_filter(street_name, street_number)