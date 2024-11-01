# orders DB
from .orders.client_dao import ClientDAO
from .orders.shop_adress_dao import ShopAdressDAO
from .orders.shop_dao import ShopDAO
from .orders.manufactures_dao import ManufacturesDAO
from .orders.service_type_dao import ServiceTypeDAO
from .orders.masters_dao import MastersDAO
from .orders.terminal_dao import TerminalDAO
from .orders.service_job_dao import ServiceJobDAO
from .orders.service_job_masters_dao import ServiceJobMastersDAO
from .orders.invoices_dao import InvoicesDAO


client_dao = ClientDAO()
shop_adress_dao = ShopAdressDAO()
shop_dao = ShopDAO()
manufactures_dao = ManufacturesDAO()
service_type_dao = ServiceTypeDAO()
masters_dao = MastersDAO()
terminal_dao = TerminalDAO()
service_job_dao = ServiceJobDAO()
service_job_masters_dao = ServiceJobMastersDAO()
invoices_dao = InvoicesDAO()
