from tkinter import Button, Entry

from src.gui.pages.login_page import LoginPage


class TestLoginPage:
    def test_login_page_default_login_credentials(self):
        login_page = LoginPage()

        assert login_page.login_credentials == {
            "email": "",
            "password": "",
            "saveEmail": "",
        }

        login_page.destroy()

    def test_login_page_default_entries(self):
        login_page = LoginPage()

        assert (
            isinstance(login_page.email_entry, Entry)
            and isinstance(login_page.password_entry, Entry)
            and isinstance(login_page.login_button, Button)
        )

        login_page.destroy()

    def test_login_default_entry_values(self):
        login_page = LoginPage()

        assert (
            login_page.email_entry.get() == "" and login_page.password_entry.get() == ""
        )

        login_page.destroy()

    def test_login_page_setters(self):
        login_page = LoginPage()

        login_page.create_login_page()
        login_page.email_entry = "tesztemail@gmail.com"
        login_page.password_entry = "tesztpassword"
        login_page.email_remember_button = 1

        assert (
            login_page.email_entry.get() == "tesztemail@gmail.com"
            and login_page.password_entry.get() == "tesztpassword"
            and login_page.email_remember_button.get() == 1
        )

        login_page.destroy()
