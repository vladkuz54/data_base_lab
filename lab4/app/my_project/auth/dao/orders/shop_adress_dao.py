from typing import List

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import Shop_Adress

class ShopAdressDAO(GeneralDAO):

    _domain_type = Shop_Adress

    def find_by_street(self, street: str) -> List[object]:
        return self._session.query(Shop_Adress).filter(Shop_Adress.street, Shop_Adress.street_number == street).all()