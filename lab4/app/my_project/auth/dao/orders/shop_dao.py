from typing import List, Dict, Any

import sqlalchemy

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import Shop


class ShopDAO(GeneralDAO):
    _domain_type = Shop

    def get_shop_by_num(self, num: int) -> List[object]:
        return self._session.query(Shop).filter(Shop.id == num).order_by(Shop.id).all()

    def get_shops_after_client(self, client_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_shops_after_client(:p1)"),
                                       {'p1': client_id}).mappings().all()
        return [dict(row) for row in result]
