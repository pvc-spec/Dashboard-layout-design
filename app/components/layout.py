import reflex as rx
from app.components.sidebar import sidebar
from app.components.navbar import navbar


def main_layout(content: rx.Component) -> rx.Component:
    return rx.el.main(
        rx.el.div(
            sidebar(),
            rx.el.div(
                navbar(),
                rx.el.main(
                    content, class_name="flex-1 p-4 md:p-6 lg:p-8 overflow-y-auto"
                ),
                class_name="flex flex-col flex-1",
            ),
            class_name="flex min-h-screen w-full bg-gray-50",
        ),
        class_name="font-['Montserrat']",
    )