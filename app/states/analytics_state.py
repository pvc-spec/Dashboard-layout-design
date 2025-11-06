import reflex as rx
from typing import TypedDict


class Metric(TypedDict):
    label: str
    value: str
    icon: str


class TopProduct(TypedDict):
    name: str
    sales: int


class RevenueData(TypedDict):
    month: str
    revenue: int


class AnalyticsState(rx.State):
    date_range: str = "Last 30 Days"
    date_range_options: list[str] = [
        "Last 7 Days",
        "Last 30 Days",
        "Last 90 Days",
        "Last Year",
    ]
    key_metrics: list[Metric] = [
        {"label": "Total Revenue", "value": "$145,231", "icon": "dollar-sign"},
        {"label": "Conversion Rate", "value": "3.2%", "icon": "users"},
        {"label": "Avg. Order Value", "value": "$89.50", "icon": "shopping-cart"},
        {"label": "Customer Lifetime Value", "value": "$1,234", "icon": "activity"},
    ]
    revenue_data: list[RevenueData] = [
        {"month": "Jan", "revenue": 12000},
        {"month": "Feb", "revenue": 14000},
        {"month": "Mar", "revenue": 18000},
        {"month": "Apr", "revenue": 15000},
        {"month": "May", "revenue": 21000},
        {"month": "Jun", "revenue": 25000},
    ]
    top_products: list[TopProduct] = [
        {"name": "Wireless Headphones", "sales": 1234},
        {"name": "Smart Watch", "sales": 987},
        {"name": "Portable Speaker", "sales": 765},
        {"name": "Ergonomic Mouse", "sales": 543},
        {"name": "Mechanical Keyboard", "sales": 432},
    ]