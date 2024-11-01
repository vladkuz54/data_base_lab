
from .orders.client_service import ClientService
from .orders.shop_adress_service import ShopAdressService
from .orders.shop_service import ShopService
from .orders.manufactures_service import ManufacturesService
from .orders.service_type_service import ServiceTypeService
from .orders.masters_service import MastersService
from .orders.terminal_service import TerminalService
from .orders.service_job_service import ServiceJobService
from .orders.service_job_masters_service import ServiceJobMastersService
from .orders.invoices_service import InvoicesService

client_service = ClientService()
shop_adress_service = ShopAdressService()
shop_service = ShopService()
manufactures_service = ManufacturesService()
service_type_service = ServiceTypeService()
masters_service = MastersService()
terminals_service = TerminalService()
service_job_service = ServiceJobService()
service_job_masters_service = ServiceJobMastersService()
invoices_service = InvoicesService()
