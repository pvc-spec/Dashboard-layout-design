import reflex as rx
from app.components.layout import main_layout
from app.components.dashboard_content import dashboard_content
from app.pages.orders import orders
from app.pages.products import products
from app.pages.customers import customers
from app.pages.analytics import analytics
from app.pages.settings import settings
from app.pages.support import support
from app.pages.login import login
from app.states.auth_state import AuthState


@rx.page(route="/", title="Dashboard", on_load=AuthState.check_login)
def index() -> rx.Component:
    return main_layout(dashboard_content())


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(login)
app.add_page(orders, on_load=AuthState.check_login)
app.add_page(products, on_load=AuthState.check_login)
app.add_page(customers, on_load=AuthState.check_login)
app.add_page(analytics, on_load=AuthState.check_login)
app.add_page(settings, on_load=AuthState.check_login)
app.add_page(support, on_load=AuthState.check_login)