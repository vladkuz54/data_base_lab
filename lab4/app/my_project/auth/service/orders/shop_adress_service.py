from lab4.app.my_project.auth.dao import shop_adress_dao
from lab4.app.my_project.auth.service.general_service import GeneralService

class ShopAdressService(GeneralService):

    _dao = shop_adress_dao
