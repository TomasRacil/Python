from tkinter import Tk
from function import sqlinitialize, loginScreen, firstTimeScreen


def main():

    # Window createtion and database initialization
    window = Tk()
    window.update()
    window.title("Password Vault")
    cursor = sqlinitialize()
    cursor.execute("SELECT * FROM masterpassword")
    if cursor.fetchall():
        loginScreen(window)
    else:
        firstTimeScreen(window)
    window.mainloop()


___main___ = main()
