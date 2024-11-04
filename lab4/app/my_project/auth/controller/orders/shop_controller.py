from lab4.app.my_project.auth.service import shop_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class ShopController(GeneralController):
    _service = shop_service

