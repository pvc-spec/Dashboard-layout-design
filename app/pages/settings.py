import reflex as rx
from app.components.layout import main_layout
from app.states.settings_state import SettingsState


def form_group(
    label: str, input_component: rx.Component, description: str
) -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name="font-semibold text-gray-800"),
        input_component,
        rx.el.p(description, class_name="text-sm text-gray-500"),
        class_name="space-y-2",
    )


def profile_settings() -> rx.Component:
    return rx.el.div(
        form_group(
            "Name",
            rx.el.input(
                default_value=SettingsState.profile_name,
                on_change=SettingsState.set_profile_name,
                class_name="w-full p-2 border border-gray-300 rounded-md",
            ),
            "This is your public display name.",
        ),
        form_group(
            "Email",
            rx.el.input(
                default_value=SettingsState.profile_email,
                on_change=SettingsState.set_profile_email,
                type="email",
                class_name="w-full p-2 border border-gray-300 rounded-md",
            ),
            "This is the email you use to log in.",
        ),
        rx.el.button(
            "Save Changes",
            on_click=rx.toast.success("Profile saved!"),
            class_name="px-4 py-2 bg-black text-white rounded-md hover:bg-gray-800",
        ),
        class_name="space-y-6",
    )


def notifications_settings() -> rx.Component:
    return rx.el.div(
        form_group(
            "Communication Emails",
            rx.el.div(
                rx.el.input(
                    type="checkbox",
                    id="marketing-emails",
                    checked=SettingsState.notifications["marketing"],
                    on_change=lambda val: SettingsState.set_notification_preference(
                        "marketing", val
                    ),
                ),
                rx.el.label(
                    "Marketing emails", htmlFor="marketing-emails", class_name="ml-2"
                ),
                class_name="flex items-center",
            ),
            "Receive emails about new products, features, and more.",
        ),
        form_group(
            "Security Emails",
            rx.el.div(
                rx.el.input(
                    type="checkbox",
                    id="security-emails",
                    checked=SettingsState.notifications["security"],
                    on_change=lambda val: SettingsState.set_notification_preference(
                        "security", val
                    ),
                ),
                rx.el.label(
                    "Security emails", htmlFor="security-emails", class_name="ml-2"
                ),
                class_name="flex items-center",
            ),
            "Receive emails about your account security.",
        ),
        rx.el.button(
            "Save Changes",
            on_click=rx.toast.success("Notifications saved!"),
            class_name="px-4 py-2 bg-black text-white rounded-md hover:bg-gray-800",
        ),
        class_name="space-y-6",
    )


def settings_content() -> rx.Component:
    return rx.el.div(
        rx.el.h1(
            "Settings", class_name="text-3xl font-bold tracking-tight text-gray-900"
        ),
        rx.el.div(
            rx.el.div(
                rx.el.button(
                    "My Profile",
                    on_click=SettingsState.set_active_tab("profile"),
                    class_name=rx.cond(
                        SettingsState.active_tab == "profile",
                        "px-3 py-2 font-semibold text-blue-600 border-b-2 border-blue-600",
                        "px-3 py-2 font-medium text-gray-600 hover:text-gray-900",
                    ),
                ),
                rx.el.button(
                    "Notifications",
                    on_click=SettingsState.set_active_tab("notifications"),
                    class_name=rx.cond(
                        SettingsState.active_tab == "notifications",
                        "px-3 py-2 font-semibold text-blue-600 border-b-2 border-blue-600",
                        "px-3 py-2 font-medium text-gray-600 hover:text-gray-900",
                    ),
                ),
                class_name="flex items-center gap-4 border-b",
            ),
            rx.el.div(
                rx.match(
                    SettingsState.active_tab,
                    ("profile", profile_settings()),
                    ("notifications", notifications_settings()),
                    rx.el.div("Select a tab"),
                ),
                class_name="p-6 bg-white rounded-b-xl border-x border-b",
            ),
            class_name="mt-6",
        ),
        class_name="p-0",
    )


@rx.page(route="/settings", title="Settings")
def settings() -> rx.Component:
    return main_layout(settings_content())