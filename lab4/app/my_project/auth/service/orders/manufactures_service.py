from typing import List

from lab4.app.my_project.auth.dao import manufactures_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class ManufacturesService(GeneralService):

    _dao = manufactures_dao