import reflex as rx
from app.components.layout import main_layout
from app.states.customer_state import CustomerState, Customer


def customer_row(customer: Customer) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.image(
                    src=f"https://api.dicebear.com/9.x/notionists/svg?seed={customer['avatar_seed']}",
                    class_name="h-10 w-10 rounded-full",
                ),
                rx.el.div(
                    rx.el.div(customer["name"], class_name="font-medium"),
                    rx.el.div(customer["email"], class_name="text-sm text-gray-500"),
                    class_name="ml-4",
                ),
                class_name="flex items-center",
            ),
            class_name="py-3 px-4",
        ),
        rx.el.td(
            rx.el.span(
                customer["status"],
                class_name=rx.cond(
                    customer["status"] == "Active",
                    "px-2 py-1 text-xs font-medium rounded-full bg-green-100 text-green-800",
                    "px-2 py-1 text-xs font-medium rounded-full bg-gray-100 text-gray-800",
                ),
            ),
            class_name="py-3 px-4",
        ),
        rx.el.td(customer["join_date"], class_name="py-3 px-4 text-sm"),
        rx.el.td(
            customer["total_orders"].to_string(),
            class_name="py-3 px-4 text-sm text-center",
        ),
        rx.el.td(
            rx.el.div(
                rx.el.button(rx.icon("eye", class_name="h-4 w-4"), variant="ghost"),
                rx.el.button(rx.icon("pencil", class_name="h-4 w-4"), variant="ghost"),
                rx.el.button(
                    rx.icon("trash-2", class_name="h-4 w-4"),
                    variant="ghost",
                    color_scheme="red",
                ),
                class_name="flex items-center justify-end gap-2",
            ),
            class_name="py-3 px-4 text-right",
        ),
        class_name="border-b border-gray-200 hover:bg-gray-50",
    )


def customers_content() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Customers",
                class_name="text-3xl font-bold tracking-tight text-gray-900",
            ),
            rx.el.button(
                rx.icon("circle_plus", class_name="h-4 w-4 mr-2"),
                "Add Customer",
                class_name="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-black text-white hover:bg-black/90 h-10 px-4 py-2",
            ),
            class_name="flex items-center justify-between mb-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        "search",
                        class_name="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400",
                    ),
                    rx.el.input(
                        placeholder="Search customers...",
                        on_change=CustomerState.set_search_query,
                        class_name="pl-10 w-full bg-white border border-gray-300 rounded-lg py-2 px-4 text-sm",
                    ),
                    class_name="relative",
                ),
                class_name="w-full max-w-sm",
            )
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Customer",
                            class_name="py-2 px-4 text-left text-sm font-semibold text-gray-600",
                        ),
                        rx.el.th(
                            "Status",
                            class_name="py-2 px-4 text-left text-sm font-semibold text-gray-600",
                        ),
                        rx.el.th(
                            "Join Date",
                            class_name="py-2 px-4 text-left text-sm font-semibold text-gray-600",
                        ),
                        rx.el.th(
                            "Total Orders",
                            class_name="py-2 px-4 text-center text-sm font-semibold text-gray-600",
                        ),
                        rx.el.th("", class_name="py-2 px-4"),
                    )
                ),
                rx.el.tbody(rx.foreach(CustomerState.filtered_customers, customer_row)),
                class_name="w-full table-auto",
            ),
            class_name="bg-white border border-gray-200 rounded-xl mt-6 overflow-hidden",
        ),
        class_name="p-0",
    )


@rx.page(route="/customers", title="Customers")
def customers() -> rx.Component:
    return main_layout(customers_content())