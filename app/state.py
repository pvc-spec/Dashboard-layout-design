import reflex as rx
from typing import TypedDict


class NavItem(TypedDict):
    label: str
    icon: str
    href: str


class CardData(TypedDict):
    title: str
    value: str
    change: str
    change_type: str
    icon: str


class DashboardState(rx.State):
    sidebar_collapsed: bool = False
    nav_items: list[NavItem] = [
        {"label": "Dashboard", "icon": "layout-dashboard", "href": "/"},
        {"label": "Orders", "icon": "shopping-cart", "href": "/orders"},
        {"label": "Products", "icon": "package", "href": "/products"},
        {"label": "Customers", "icon": "users", "href": "/customers"},
        {"label": "Analytics", "icon": "bar-chart-2", "href": "/analytics"},
    ]
    main_nav_items: list[NavItem] = [
        {"label": "Settings", "icon": "settings", "href": "/settings"},
        {"label": "Support", "icon": "life-buoy", "href": "/support"},
    ]
    card_data: list[CardData] = [
        {
            "title": "Total Revenue",
            "value": "$45,231.89",
            "change": "+20.1% from last month",
            "change_type": "increase",
            "icon": "dollar-sign",
        },
        {
            "title": "Subscriptions",
            "value": "+2350",
            "change": "+180.1% from last month",
            "change_type": "increase",
            "icon": "users",
        },
        {
            "title": "Sales",
            "value": "+12,234",
            "change": "+19% from last month",
            "change_type": "increase",
            "icon": "credit-card",
        },
        {
            "title": "Active Now",
            "value": "+573",
            "change": "+201 since last hour",
            "change_type": "increase",
            "icon": "activity",
        },
    ]

    @rx.event
    def toggle_sidebar(self):
        self.sidebar_collapsed = not self.sidebar_collapsed