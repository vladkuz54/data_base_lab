from lab4.app.my_project.auth.service import manufactures_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class ManufacturesController(GeneralController):

    _service = manufactures_service

