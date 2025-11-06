import reflex as rx
from typing import TypedDict


class SettingsState(rx.State):
    active_tab: str = "profile"
    profile_name: str = "Admin User"
    profile_email: str = "admin@example.com"
    notifications: dict[str, bool] = {"marketing": True, "security": True}

    @rx.event
    def set_notification_preference(self, key: str, value: bool):
        self.notifications[key] = value