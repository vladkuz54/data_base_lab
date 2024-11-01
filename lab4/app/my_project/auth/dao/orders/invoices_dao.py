from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import Invoices


class InvoicesDAO(GeneralDAO):
    _domain_type = Invoices
