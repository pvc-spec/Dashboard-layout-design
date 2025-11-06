import reflex as rx
from app.components.layout import main_layout
from app.states.order_state import OrderState, Order, OrderStat


def status_badge(status: str) -> rx.Component:
    color_scheme = {
        "Pending": "bg-yellow-100 text-yellow-800",
        "Processing": "bg-blue-100 text-blue-800",
        "Shipped": "bg-indigo-100 text-indigo-800",
        "Delivered": "bg-green-100 text-green-800",
        "Cancelled": "bg-gray-100 text-gray-800",
    }
    return rx.el.span(
        status,
        class_name=f"px-2 py-1 text-xs font-medium rounded-full {color_scheme.get(status, 'bg-gray-100 text-gray-800')}",
    )


def order_row(order: Order) -> rx.Component:
    return rx.el.tr(
        rx.el.td(order["id"], class_name="py-3 px-4 font-medium"),
        rx.el.td(
            rx.el.div(
                rx.image(
                    src=f"https://api.dicebear.com/9.x/initials/svg?seed={order['avatar_seed']}",
                    class_name="h-8 w-8 rounded-full mr-3",
                ),
                rx.el.span(order["customer_name"]),
                class_name="flex items-center",
            ),
            class_name="py-3 px-4",
        ),
        rx.el.td(order["date"], class_name="py-3 px-4 text-sm"),
        rx.el.td(status_badge(order["status"]), class_name="py-3 px-4"),
        rx.el.td(order["total"], class_name="py-3 px-4 text-right font-medium"),
        rx.el.td(
            rx.el.div(
                rx.el.button(
                    rx.icon("eye", class_name="h-4 w-4"),
                    class_name="p-1 hover:bg-gray-100 rounded-md",
                ),
                rx.el.button(
                    rx.icon("pencil", class_name="h-4 w-4"),
                    class_name="p-1 hover:bg-gray-100 rounded-md",
                ),
                rx.el.button(
                    rx.icon("trash-2", class_name="h-4 w-4 text-red-500"),
                    class_name="p-1 hover:bg-red-50 rounded-md",
                ),
                class_name="flex items-center justify-end gap-2",
            ),
            class_name="py-3 px-4",
        ),
        class_name="border-b border-gray-200 hover:bg-gray-50/50",
    )


def stat_card(stat: OrderStat) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(stat["label"], class_name="text-sm font-medium text-gray-500"),
            rx.icon(stat["icon"], class_name="h-4 w-4 text-gray-400"),
            class_name="flex items-center justify-between",
        ),
        rx.el.p(stat["value"], class_name="text-2xl font-bold text-gray-900 mt-1"),
        class_name="bg-white p-5 rounded-xl border border-gray-200 shadow-sm",
    )


def orders_content() -> rx.Component:
    return rx.el.div(
        rx.el.h1(
            "Orders", class_name="text-3xl font-bold tracking-tight text-gray-900 mb-6"
        ),
        rx.el.div(
            rx.foreach(OrderState.stats, stat_card),
            class_name="grid gap-4 md:grid-cols-2 lg:grid-cols-4 mb-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        "search",
                        class_name="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400",
                    ),
                    rx.el.input(
                        placeholder="Search orders...",
                        on_change=OrderState.set_search_query.debounce(300),
                        class_name="pl-10 w-full bg-white border border-gray-300 rounded-lg py-2 px-4 text-sm",
                    ),
                    class_name="relative w-full max-w-sm",
                ),
                rx.el.div(
                    rx.el.select(
                        rx.foreach(
                            OrderState.status_options,
                            lambda opt: rx.el.option(opt, value=opt),
                        ),
                        value=OrderState.status_filter,
                        on_change=OrderState.set_status_filter,
                        class_name="text-sm font-medium border-gray-300 rounded-lg shadow-sm w-full md:w-auto",
                    ),
                    rx.el.button(
                        rx.icon("circle_plus", class_name="h-4 w-4 mr-2"),
                        "Add Order",
                        class_name="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium bg-black text-white hover:bg-black/90 h-10 px-4 py-2",
                    ),
                    class_name="flex items-center gap-2",
                ),
                class_name="flex flex-col md:flex-row items-center justify-between gap-4",
            ),
            rx.el.div(
                rx.el.table(
                    rx.el.thead(
                        rx.el.tr(
                            rx.el.th(
                                "Order ID",
                                class_name="py-3 px-4 text-left text-sm font-semibold text-gray-600",
                            ),
                            rx.el.th(
                                "Customer",
                                class_name="py-3 px-4 text-left text-sm font-semibold text-gray-600",
                            ),
                            rx.el.th(
                                "Date",
                                class_name="py-3 px-4 text-left text-sm font-semibold text-gray-600",
                            ),
                            rx.el.th(
                                "Status",
                                class_name="py-3 px-4 text-left text-sm font-semibold text-gray-600",
                            ),
                            rx.el.th(
                                "Total",
                                class_name="py-3 px-4 text-right text-sm font-semibold text-gray-600",
                            ),
                            rx.el.th("", class_name="py-3 px-4"),
                        )
                    ),
                    rx.el.tbody(rx.foreach(OrderState.filtered_orders, order_row)),
                    class_name="w-full table-auto",
                ),
                class_name="bg-white border border-gray-200 rounded-xl mt-6 overflow-hidden shadow-sm",
            ),
            class_name="p-0",
        ),
        class_name="p-0",
    )


@rx.page(route="/orders", title="Orders")
def orders() -> rx.Component:
    return main_layout(orders_content())