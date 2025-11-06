import reflex as rx
from app.components.layout import main_layout
from app.states.product_state import ProductState, Product, ProductStat


def stat_card(stat: ProductStat) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(stat["label"], class_name="text-sm font-medium text-gray-500"),
            rx.icon(stat["icon"], class_name="h-4 w-4 text-gray-400"),
            class_name="flex items-center justify-between",
        ),
        rx.el.p(stat["value"], class_name="text-2xl font-bold text-gray-900 mt-1"),
        class_name="bg-white p-5 rounded-xl border border-gray-200 shadow-sm",
    )


def product_card(product: Product) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.image(
                src=product["image_url"],
                class_name="w-full h-40 object-cover rounded-t-lg",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h3(product["name"], class_name="font-semibold text-lg"),
                    rx.el.p(
                        f"${product['price']:.2f}", class_name="font-bold text-blue-600"
                    ),
                    class_name="flex justify-between items-start",
                ),
                rx.el.p(product["category"], class_name="text-sm text-gray-500"),
                rx.el.div(
                    rx.el.span(
                        f"{product['stock']} in stock",
                        class_name=rx.cond(
                            product["stock"] > 50,
                            "text-green-600",
                            rx.cond(
                                product["stock"] > 0, "text-yellow-600", "text-red-600"
                            ),
                        ),
                    ),
                    class_name="text-xs font-medium mt-2",
                ),
                class_name="p-4",
            ),
            class_name="bg-white rounded-lg border border-gray-200 shadow-sm overflow-hidden hover:shadow-lg transition-shadow duration-300",
        )
    )


def products_content() -> rx.Component:
    return rx.el.div(
        rx.el.h1(
            "Products",
            class_name="text-3xl font-bold tracking-tight text-gray-900 mb-6",
        ),
        rx.el.div(
            rx.foreach(ProductState.stats, stat_card),
            class_name="grid gap-4 md:grid-cols-2 lg:grid-cols-4 mb-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon(
                    "search",
                    class_name="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400",
                ),
                rx.el.input(
                    placeholder="Search products...",
                    on_change=ProductState.set_search_query.debounce(300),
                    class_name="pl-10 w-full bg-white border border-gray-300 rounded-lg py-2 px-4 text-sm",
                ),
                class_name="relative w-full max-w-sm",
            ),
            rx.el.div(
                rx.el.select(
                    rx.foreach(
                        ProductState.category_options,
                        lambda opt: rx.el.option(opt, value=opt),
                    ),
                    value=ProductState.category_filter,
                    on_change=ProductState.set_category_filter,
                    class_name="text-sm font-medium border-gray-300 rounded-lg shadow-sm w-full md:w-auto",
                ),
                rx.el.button(
                    rx.icon("circle_plus", class_name="h-4 w-4 mr-2"),
                    "Add Product",
                    class_name="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium bg-black text-white hover:bg-black/90 h-10 px-4 py-2",
                ),
                class_name="flex items-center gap-2",
            ),
            class_name="flex flex-col md:flex-row items-center justify-between gap-4 mb-6",
        ),
        rx.el.div(
            rx.foreach(ProductState.filtered_products, product_card),
            class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6",
        ),
        class_name="p-0",
    )


@rx.page(route="/products", title="Products")
def products() -> rx.Component:
    return main_layout(products_content())