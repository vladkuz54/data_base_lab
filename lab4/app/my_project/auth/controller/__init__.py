from .orders.client_controller import ClientController
from .orders.shop_adress_controller import ShopAdressController
from .orders.shop_controller import ShopController
from .orders.manufactures_controller import ManufacturesController
from .orders.service_type_controller import ServiceTypeController
from .orders.masters_controller import MastersController
from .orders.terminal_controller import TerminalController
from .orders.service_job_controller import ServiceJobController
from .orders.service_job_masters_contoller import ServiceJobMastersController
from .orders.invoices_controller import InvoicesController

client_controller = ClientController()
shop_adress_controller = ShopAdressController()
shop_controller = ShopController()
manufactures_controller = ManufacturesController()
service_type_controller = ServiceTypeController()
masters_controller = MastersController()
terminal_controller = TerminalController()
service_job_controller = ServiceJobController()
service_job_masters_controller = ServiceJobMastersController()
invoices_controller = InvoicesController()
