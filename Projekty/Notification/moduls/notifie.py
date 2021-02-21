from win10toast import ToastNotifier

#funkce vytvari windows 10 notifikaci s nadpisem a zpravou kterou dostala
#jako ikonka notifikace se pouzije obrazek ulozeny s programem
def notifie(title, message):
	toaster = ToastNotifier()
	toaster.show_toast(title, str(message), icon_path="./skull.ico", duration=10)