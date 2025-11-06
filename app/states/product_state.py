import reflex as rx
from typing import TypedDict


class Product(TypedDict):
    id: int
    name: str
    category: str
    price: float
    stock: int
    image_url: str


class ProductStat(TypedDict):
    label: str
    value: str
    icon: str


class ProductState(rx.State):
    products: list[Product] = [
        {
            "id": 1,
            "name": "Wireless Headphones",
            "category": "Electronics",
            "price": 99.99,
            "stock": 120,
            "image_url": "/placeholder.svg",
        },
        {
            "id": 2,
            "name": "Smart Watch",
            "category": "Electronics",
            "price": 199.99,
            "stock": 80,
            "image_url": "/placeholder.svg",
        },
        {
            "id": 3,
            "name": "Leather Backpack",
            "category": "Fashion",
            "price": 79.99,
            "stock": 50,
            "image_url": "/placeholder.svg",
        },
        {
            "id": 4,
            "name": "Organic Coffee Beans",
            "category": "Groceries",
            "price": 19.99,
            "stock": 200,
            "image_url": "/placeholder.svg",
        },
        {
            "id": 5,
            "name": "Yoga Mat",
            "category": "Sports",
            "price": 29.99,
            "stock": 150,
            "image_url": "/placeholder.svg",
        },
        {
            "id": 6,
            "name": "Desk Lamp",
            "category": "Home Goods",
            "price": 49.99,
            "stock": 90,
            "image_url": "/placeholder.svg",
        },
        {
            "id": 7,
            "name": 'Novel - "The Great Gatsby"',
            "category": "Books",
            "price": 14.99,
            "stock": 300,
            "image_url": "/placeholder.svg",
        },
        {
            "id": 8,
            "name": "Bluetooth Speaker",
            "category": "Electronics",
            "price": 69.99,
            "stock": 75,
            "image_url": "/placeholder.svg",
        },
    ]
    search_query: str = ""
    category_filter: str = "All"

    @rx.var
    def category_options(self) -> list[str]:
        return ["All"] + sorted(list({p["category"] for p in self.products}))

    @rx.var
    def filtered_products(self) -> list[Product]:
        return [
            product
            for product in self.products
            if (
                self.category_filter == "All"
                or product["category"] == self.category_filter
            )
            and (
                self.search_query.lower() in product["name"].lower()
                or self.search_query.lower() in product["category"].lower()
            )
        ]

    @rx.var
    def stats(self) -> list[ProductStat]:
        total_products = len(self.products)
        low_stock = sum((1 for p in self.products if 0 < p["stock"] < 50))
        out_of_stock = sum((1 for p in self.products if p["stock"] == 0))
        total_value = sum((p["price"] * p["stock"] for p in self.products))
        return [
            {
                "label": "Total Products",
                "value": str(total_products),
                "icon": "package",
            },
            {"label": "Low Stock", "value": str(low_stock), "icon": "trending-down"},
            {"label": "Out of Stock", "value": str(out_of_stock), "icon": "package-x"},
            {
                "label": "Total Stock Value",
                "value": f"${total_value:,.2f}",
                "icon": "dollar-sign",
            },
        ]