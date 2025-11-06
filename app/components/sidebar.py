import reflex as rx
from app.state import DashboardState, NavItem


def nav_item(item: NavItem, collapsed: rx.Var[bool]) -> rx.Component:
    return rx.el.a(
        rx.icon(item["icon"], class_name="h-5 w-5 shrink-0"),
        rx.cond(
            collapsed, rx.fragment(), rx.el.span(item["label"], class_name="truncate")
        ),
        href=item["href"],
        class_name="flex items-center gap-3 rounded-lg px-3 py-2 text-gray-500 transition-all hover:text-gray-900 hover:bg-gray-100",
    )


def sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.icon("mountain", class_name="h-6 w-6 text-blue-600"),
                    rx.cond(
                        DashboardState.sidebar_collapsed,
                        rx.fragment(),
                        rx.el.span("ACME Inc.", class_name="font-semibold text-lg"),
                    ),
                    href="#",
                    class_name="flex items-center gap-2 font-semibold text-gray-900",
                ),
                rx.cond(DashboardState.sidebar_collapsed, rx.fragment(), rx.el.span()),
                class_name="flex h-16 items-center justify-between border-b px-4 shrink-0",
            ),
            rx.el.nav(
                rx.foreach(
                    DashboardState.nav_items,
                    lambda item: nav_item(item, DashboardState.sidebar_collapsed),
                ),
                class_name="flex flex-col gap-2 p-4 text-sm font-medium",
            ),
        ),
        rx.el.div(
            rx.el.nav(
                rx.foreach(
                    DashboardState.main_nav_items,
                    lambda item: nav_item(item, DashboardState.sidebar_collapsed),
                ),
                class_name="flex flex-col gap-2 p-4 text-sm font-medium",
            )
        ),
        class_name=rx.cond(
            DashboardState.sidebar_collapsed,
            "hidden md:flex flex-col justify-between border-r bg-white transition-all w-20",
            "hidden md:flex flex-col justify-between border-r bg-white transition-all w-64",
        ),
    )