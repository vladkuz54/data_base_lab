from lab4.app.my_project.auth.service import invoices_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class InvoicesController(GeneralController):

    _service = invoices_service