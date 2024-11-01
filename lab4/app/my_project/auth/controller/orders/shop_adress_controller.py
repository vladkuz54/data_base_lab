from lab4.app.my_project.auth.service import shop_adress_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class ShopAdressController(GeneralController):
    _service = shop_adress_service
