from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:

    app.register_blueprint(err_handler_bp)

    from .orders.shop_route import shop_bp
    from .orders.client_route import client_bp
    from .orders.shop_adress_route import shop_adress_bp
    from .orders.manufactures_route import manufactures_bp
    from .orders.service_type_route import service_type_bp
    from .orders.masters_route import masters_bp
    from .orders.terminal_route import terminal_bp
    from .orders.service_job_route import service_job_bp
    from .orders.service_job_masters_route import service_job_masters_bp
    from .orders.invoices_route import invoices_bp

    app.register_blueprint(shop_bp)
    app.register_blueprint(client_bp)
    app.register_blueprint(shop_adress_bp)
    app.register_blueprint(manufactures_bp)
    app.register_blueprint(service_type_bp)
    app.register_blueprint(masters_bp)
    app.register_blueprint(terminal_bp)
    app.register_blueprint(service_job_bp)
    app.register_blueprint(service_job_masters_bp)
    app.register_blueprint(invoices_bp)
