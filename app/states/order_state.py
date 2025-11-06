import reflex as rx
from typing import TypedDict


class Order(TypedDict):
    id: str
    customer_name: str
    date: str
    status: str
    total: str
    avatar_seed: str


class OrderStat(TypedDict):
    label: str
    value: str
    icon: str


class OrderState(rx.State):
    orders: list[Order] = [
        {
            "id": "#3210",
            "customer_name": "Olivia Martin",
            "date": "2023-11-20",
            "status": "Shipped",
            "total": "$42.25",
            "avatar_seed": "Olivia Martin",
        },
        {
            "id": "#3209",
            "customer_name": "John Doe",
            "date": "2023-11-19",
            "status": "Delivered",
            "total": "$89.99",
            "avatar_seed": "John Doe",
        },
        {
            "id": "#3208",
            "customer_name": "Jane Smith",
            "date": "2023-11-18",
            "status": "Processing",
            "total": "$120.50",
            "avatar_seed": "Jane Smith",
        },
        {
            "id": "#3207",
            "customer_name": "Sam Wilson",
            "date": "2023-11-17",
            "status": "Pending",
            "total": "$35.00",
            "avatar_seed": "Sam Wilson",
        },
        {
            "id": "#3206",
            "customer_name": "Alice Johnson",
            "date": "2023-11-16",
            "status": "Shipped",
            "total": "$75.60",
            "avatar_seed": "Alice Johnson",
        },
        {
            "id": "#3205",
            "customer_name": "Michael Brown",
            "date": "2023-11-15",
            "status": "Delivered",
            "total": "$250.00",
            "avatar_seed": "Michael Brown",
        },
        {
            "id": "#3204",
            "customer_name": "Emily Davis",
            "date": "2023-11-14",
            "status": "Cancelled",
            "total": "$55.00",
            "avatar_seed": "Emily Davis",
        },
    ]
    stats: list[OrderStat] = [
        {"label": "Total Orders", "value": "1,234", "icon": "package"},
        {"label": "Pending Orders", "value": "12", "icon": "loader"},
        {"label": "Shipped Orders", "value": "890", "icon": "truck"},
        {"label": "Revenue", "value": "$120.5k", "icon": "dollar-sign"},
    ]
    search_query: str = ""
    status_filter: str = "All"
    status_options: list[str] = [
        "All",
        "Pending",
        "Processing",
        "Shipped",
        "Delivered",
        "Cancelled",
    ]

    @rx.var
    def filtered_orders(self) -> list[Order]:
        query_lower = self.search_query.lower()
        return [
            order
            for order in self.orders
            if (self.status_filter == "All" or order["status"] == self.status_filter)
            and (
                query_lower in order["id"].lower()
                or query_lower in order["customer_name"].lower()
                or query_lower in order["date"].lower()
            )
        ]