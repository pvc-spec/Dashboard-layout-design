import reflex as rx
from typing import TypedDict


class Customer(TypedDict):
    name: str
    email: str
    status: str
    join_date: str
    total_orders: int
    avatar_seed: str


class CustomerState(rx.State):
    search_query: str = ""
    customers: list[Customer] = [
        {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "status": "Active",
            "join_date": "2023-01-15",
            "total_orders": 24,
            "avatar_seed": "John Doe",
        },
        {
            "name": "Jane Smith",
            "email": "jane.smith@example.com",
            "status": "Active",
            "join_date": "2023-02-20",
            "total_orders": 15,
            "avatar_seed": "Jane Smith",
        },
        {
            "name": "Sam Wilson",
            "email": "sam.wilson@example.com",
            "status": "Inactive",
            "join_date": "2023-03-10",
            "total_orders": 5,
            "avatar_seed": "Sam Wilson",
        },
        {
            "name": "Alice Johnson",
            "email": "alice.johnson@example.com",
            "status": "Active",
            "join_date": "2023-04-05",
            "total_orders": 32,
            "avatar_seed": "Alice Johnson",
        },
        {
            "name": "Michael Brown",
            "email": "michael.brown@example.com",
            "status": "Active",
            "join_date": "2023-05-12",
            "total_orders": 18,
            "avatar_seed": "Michael Brown",
        },
        {
            "name": "Emily Davis",
            "email": "emily.davis@example.com",
            "status": "Inactive",
            "join_date": "2023-06-25",
            "total_orders": 3,
            "avatar_seed": "Emily Davis",
        },
        {
            "name": "David Miller",
            "email": "david.miller@example.com",
            "status": "Active",
            "join_date": "2023-07-01",
            "total_orders": 45,
            "avatar_seed": "David Miller",
        },
        {
            "name": "Sarah Garcia",
            "email": "sarah.garcia@example.com",
            "status": "Active",
            "join_date": "2023-08-18",
            "total_orders": 29,
            "avatar_seed": "Sarah Garcia",
        },
        {
            "name": "Robert Rodriguez",
            "email": "robert.rodriguez@example.com",
            "status": "Active",
            "join_date": "2023-09-02",
            "total_orders": 11,
            "avatar_seed": "Robert Rodriguez",
        },
        {
            "name": "Linda Martinez",
            "email": "linda.martinez@example.com",
            "status": "Inactive",
            "join_date": "2023-10-30",
            "total_orders": 1,
            "avatar_seed": "Linda Martinez",
        },
    ]

    @rx.var
    def filtered_customers(self) -> list[Customer]:
        if not self.search_query:
            return self.customers
        return [
            customer
            for customer in self.customers
            if self.search_query.lower() in customer["name"].lower()
            or self.search_query.lower() in customer["email"].lower()
        ]