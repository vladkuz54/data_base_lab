from typing import List

from lab4.app.my_project.auth.service import client_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class ClientController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = client_service

    

