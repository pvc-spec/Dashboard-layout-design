import reflex as rx
from app.states.auth_state import AuthState


def login_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon("mountain", class_name="h-8 w-8 text-blue-600"),
                rx.el.h1("ACME Inc.", class_name="text-2xl font-bold"),
                class_name="flex items-center justify-center gap-2 mb-8",
            ),
            rx.el.h2("Login", class_name="text-2xl font-bold text-center mb-1"),
            rx.el.p(
                "Enter your credentials to access the dashboard.",
                class_name="text-sm text-gray-500 text-center mb-6",
            ),
            rx.el.form(
                rx.el.div(
                    rx.el.label("Username", class_name="text-sm font-medium"),
                    rx.el.input(
                        name="username",
                        placeholder="admin",
                        class_name="w-full p-2 mt-1 border border-gray-300 rounded-md",
                    ),
                    class_name="space-y-1",
                ),
                rx.el.div(
                    rx.el.label("Password", class_name="text-sm font-medium"),
                    rx.el.div(
                        rx.el.input(
                            name="password",
                            placeholder="password",
                            type=rx.cond(AuthState.show_password, "text", "password"),
                            class_name="w-full p-2 mt-1 border border-gray-300 rounded-md pr-10",
                        ),
                        rx.el.button(
                            rx.icon(
                                tag=rx.cond(AuthState.show_password, "eye-off", "eye"),
                                class_name="h-5 w-5 text-gray-400",
                            ),
                            on_click=AuthState.toggle_password_visibility,
                            class_name="absolute inset-y-0 right-0 flex items-center justify-center h-full px-3",
                            type="button",
                        ),
                        class_name="relative mt-1",
                    ),
                    class_name="space-y-1",
                ),
                rx.el.button(
                    "Login",
                    type="submit",
                    class_name="w-full mt-6 px-4 py-2 bg-black text-white rounded-md hover:bg-gray-800 font-semibold",
                ),
                on_submit=AuthState.login,
                class_name="space-y-4",
            ),
            class_name="w-full max-w-sm p-8 bg-white rounded-xl border border-gray-200 shadow-sm",
        ),
        class_name="flex min-h-screen w-full items-center justify-center bg-gray-50 font-['Montserrat']",
    )


@rx.page(route="/login", title="Login")
def login() -> rx.Component:
    return login_page()