import reflex as rx
from app.state import DashboardState, CardData


def stat_card(card: CardData) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(
                card["title"],
                class_name="text-sm font-medium text-gray-500 tracking-tight",
            ),
            rx.icon(card["icon"], class_name="h-4 w-4 text-gray-400"),
            class_name="flex items-center justify-between space-y-0 pb-2",
        ),
        rx.el.div(
            rx.el.p(card["value"], class_name="text-2xl font-bold text-gray-900"),
            rx.el.p(card["change"], class_name="text-xs text-gray-500"),
            class_name="mt-1",
        ),
        class_name="bg-white p-6 rounded-xl border border-gray-200 shadow-sm hover:shadow-lg transition-shadow duration-300",
    )


def dashboard_content() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.foreach(DashboardState.card_data, stat_card),
            class_name="grid gap-4 md:grid-cols-2 lg:grid-cols-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "Recent Sales", class_name="text-lg font-semibold text-gray-900"
                    ),
                    rx.el.p(
                        "You made 265 sales this month.",
                        class_name="text-sm text-gray-500 mt-1",
                    ),
                    class_name="p-6",
                ),
                rx.el.div(
                    rx.el.div(
                        class_name="w-full h-64 bg-gray-100 rounded-b-xl flex items-center justify-center"
                    )
                ),
                class_name="bg-white rounded-xl border border-gray-200 shadow-sm",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "Overview", class_name="text-lg font-semibold text-gray-900"
                    ),
                    class_name="p-6",
                ),
                rx.el.div(
                    rx.el.div(
                        class_name="w-full h-64 bg-gray-100 rounded-b-xl flex items-center justify-center"
                    )
                ),
                class_name="bg-white rounded-xl border border-gray-200 shadow-sm",
            ),
            class_name="grid gap-4 md:grid-cols-2",
        ),
        class_name="space-y-4",
    )