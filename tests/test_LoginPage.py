from tkinter import Button, Entry

from src.gui.pages.loginPage import LoginPage


class Test_LoginPage:
    def testLoginPageDefaultLoginCredentials(self):
        loginpage = LoginPage()

        assert loginpage.loginCredentials == {
            "email": "",
            "password": "",
            "saveEmail": "",
        }

        loginpage.destroy()

    def testLoginPageDefaultEntries(self):
        loginpage = LoginPage()

        assert (
            isinstance(loginpage.emailEntry, Entry)
            and isinstance(loginpage.passwordEntry, Entry)
            and isinstance(loginpage.loginButton, Button)
        )

        loginpage.destroy()

    def testLoginDefaultEntryValues(self):
        loginpage = LoginPage()

        assert loginpage.emailEntry.get() == "" and loginpage.passwordEntry.get() == ""

        loginpage.destroy()

    def testCreateLoginPage(self):
        loginpage = LoginPage()

        loginpage.createLoginPage()
        loginpage.emailEntry = "tesztemail@gmail.com"
        loginpage.passwordEntry = "tesztpassword"
        loginpage.emailRememberButton = 1
        loginpage.after(2000, loginpage.loginButton.invoke())

        loginpage.startMainLoop()

        assert loginpage.loginCredentials == {
            "email": "tesztemail@gmail.com",
            "password": "tesztpassword",
            "saveEmail": 1,
        }

    def testLoginPageSetters(self):
        loginpage = LoginPage()

        loginpage.createLoginPage()
        loginpage.emailEntry = "tesztemail@gmail.com"
        loginpage.passwordEntry = "tesztpassword"
        loginpage.emailRememberButton = 1

        assert (
            loginpage.emailEntry.get() == "tesztemail@gmail.com"
            and loginpage.passwordEntry.get() == "tesztpassword"
            and loginpage.emailRememberButton.get() == 1
        )

        loginpage.destroy()
