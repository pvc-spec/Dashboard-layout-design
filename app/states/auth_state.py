import reflex as rx


class AuthState(rx.State):
    is_authenticated: bool = False
    username: str = ""
    password: str = ""
    error_message: str = ""
    show_password: bool = False

    @rx.event
    def login(self, form_data: dict[str, str]):
        self.username = form_data.get("username", "")
        self.password = form_data.get("password", "")
        if self.username == "admin" and self.password == "password":
            self.is_authenticated = True
            self.error_message = ""
            self.password = ""
            return rx.redirect("/")
        else:
            self.error_message = "Invalid username or password."
            self.password = ""
            return rx.toast.error(self.error_message)

    @rx.event
    def logout(self):
        self.is_authenticated = False
        self.username = ""
        self.password = ""
        return rx.redirect("/login")

    @rx.event
    def check_login(self):
        if not self.is_authenticated:
            return rx.redirect("/login")

    @rx.event
    def toggle_password_visibility(self):
        self.show_password = not self.show_password