from lab4.app.my_project.auth.service import masters_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class MastersController(GeneralController):
    _service = masters_service
