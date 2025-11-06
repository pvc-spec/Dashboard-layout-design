import reflex as rx
from app.components.layout import main_layout
from app.states.support_state import SupportState, FAQItem


def faq_item(item: FAQItem) -> rx.Component:
    return rx.el.div(
        rx.el.h3(item["question"], class_name="font-semibold text-lg"),
        rx.el.p(item["answer"], class_name="text-gray-600 mt-1"),
        class_name="py-4",
    )


def support_content() -> rx.Component:
    return rx.el.div(
        rx.el.h1(
            "Support", class_name="text-3xl font-bold tracking-tight text-gray-900"
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Contact Us", class_name="text-2xl font-semibold text-gray-800"
                ),
                rx.el.p(
                    "Have a question? Fill out the form below and we'll get back to you.",
                    class_name="text-gray-600 mt-2",
                ),
                rx.el.form(
                    rx.el.div(
                        rx.el.label("Email", htmlFor="email", class_name="font-medium"),
                        rx.el.input(
                            type="email",
                            id="email",
                            placeholder="you@example.com",
                            class_name="w-full p-2 mt-1 border border-gray-300 rounded-md",
                        ),
                        class_name="space-y-1",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Subject", htmlFor="subject", class_name="font-medium"
                        ),
                        rx.el.input(
                            id="subject",
                            placeholder="How can we help?",
                            class_name="w-full p-2 mt-1 border border-gray-300 rounded-md",
                        ),
                        class_name="space-y-1",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Message", htmlFor="message", class_name="font-medium"
                        ),
                        rx.el.textarea(
                            id="message",
                            placeholder="Your message...",
                            class_name="w-full p-2 mt-1 border border-gray-300 rounded-md h-32",
                        ),
                        class_name="space-y-1",
                    ),
                    rx.el.button(
                        "Send Message",
                        type="submit",
                        class_name="w-full px-4 py-2 bg-black text-white rounded-md hover:bg-gray-800",
                    ),
                    on_submit=lambda form_data: rx.toast.success("Message sent!"),
                    reset_on_submit=True,
                    class_name="space-y-4 mt-6",
                ),
                class_name="p-6 bg-white rounded-xl border border-gray-200 shadow-sm",
            ),
            rx.el.div(
                rx.el.h2(
                    "Frequently Asked Questions",
                    class_name="text-2xl font-semibold text-gray-800",
                ),
                rx.el.div(
                    rx.foreach(SupportState.faq_items, faq_item),
                    class_name="divide-y divide-gray-200 mt-4",
                ),
                class_name="p-6 bg-white rounded-xl border border-gray-200 shadow-sm",
            ),
            class_name="grid md:grid-cols-2 gap-8 mt-8",
        ),
        class_name="p-0",
    )


@rx.page(route="/support", title="Support")
def support() -> rx.Component:
    return main_layout(support_content())