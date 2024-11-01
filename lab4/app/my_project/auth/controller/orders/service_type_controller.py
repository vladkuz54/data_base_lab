from lab4.app.my_project.auth.service import service_type_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class ServiceTypeController(GeneralController):

    _service = service_type_service