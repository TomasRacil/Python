from win10toast import ToastNotifier

def notifie(title, message):
	toaster = ToastNotifier()
	toaster.show_toast(title, str(message), icon_path="./skull.ico", duration=10)