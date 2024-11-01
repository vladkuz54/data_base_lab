from lab4.app.my_project.auth.dao import invoices_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class InvoicesService(GeneralService):

    _dao = invoices_dao