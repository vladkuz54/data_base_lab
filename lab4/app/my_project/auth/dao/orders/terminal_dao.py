from typing import List, Dict, Any

import sqlalchemy

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import Terminal


class TerminalDAO(GeneralDAO):

    _domain_type = Terminal

    def get_terminals_after_shop(self, shop_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_terminals_after_shop(:p1)"),
                                       {'p1': shop_id}).mappings().all()
        return [dict(row) for row in result]

    def get_terminals_after_manufacturer(self, manufactures_id) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_terminals_after_manufacturer(:p1)"),
                                       {'p1': manufactures_id}).mappings().all()
        return [dict(row) for row in result]
