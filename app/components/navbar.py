import reflex as rx
from app.state import DashboardState
from app.states.auth_state import AuthState


def navbar() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.button(
                rx.icon(
                    "panel-left",
                    class_name=rx.cond(
                        DashboardState.sidebar_collapsed,
                        "h-5 w-5 text-gray-600 transition-transform rotate-180",
                        "h-5 w-5 text-gray-600 transition-transform",
                    ),
                ),
                on_click=DashboardState.toggle_sidebar,
                class_name="p-2 rounded-md hover:bg-gray-100",
                aria_label="Toggle sidebar",
            )
        ),
        rx.el.div(
            rx.el.form(
                rx.el.div(
                    rx.icon(
                        "search",
                        class_name="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400",
                    ),
                    rx.el.input(
                        type="search",
                        placeholder="Search...",
                        class_name="w-full bg-white pl-10 pr-4 py-2 text-sm rounded-lg border border-gray-200 focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all",
                    ),
                    class_name="relative w-full max-w-sm",
                )
            ),
            rx.el.button(
                rx.icon("bell", class_name="h-5 w-5"),
                class_name="p-2 rounded-full text-gray-600 hover:text-gray-900 hover:bg-gray-100 relative",
                aria_label="Notifications",
            ),
            rx.el.button(
                rx.image(
                    src=f"https://api.dicebear.com/9.x/initials/svg?seed=Admin",
                    class_name="h-8 w-8 rounded-full",
                ),
                class_name="rounded-full border-2 border-transparent hover:border-blue-500 focus:outline-none focus:border-blue-500 transition",
                aria_label="User menu",
            ),
            rx.el.button(
                rx.icon("log-out", class_name="h-5 w-5"),
                on_click=AuthState.logout,
                class_name="p-2 rounded-full text-gray-600 hover:text-gray-900 hover:bg-gray-100",
                aria_label="Logout",
            ),
            class_name="flex items-center gap-4",
        ),
        class_name="sticky top-0 z-10 flex h-16 items-center justify-between gap-4 border-b bg-white/95 backdrop-blur-sm px-4 md:px-6 shadow-sm",
    )