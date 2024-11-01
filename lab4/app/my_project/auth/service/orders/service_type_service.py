from lab4.app.my_project.auth.dao import service_type_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class ServiceTypeService(GeneralService):

    _dao = service_type_dao