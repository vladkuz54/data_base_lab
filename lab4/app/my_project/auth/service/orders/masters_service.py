from lab4.app.my_project.auth.dao import masters_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class MastersService(GeneralService):

    _dao = masters_dao