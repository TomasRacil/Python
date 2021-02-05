import socket
from _thread import *
import pickle #umožnuje nám poslat objekt ve formě jedniček a nul a poslat ji přes internet a potom ji zpětně přeměnime na objekt
from hra import Hra

server = "192.168.14.214"
port = 5555
#nadefinujeme typy připojení(ipv4,TCP protocol)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#přiřadíme portu adresu a pokut bude nějaká chyba objeví se nám
try:
	s.bind((server, port))
except socket.error as e:
	str(e)

s.listen(2) #omezení počtu hráču
print("Čeká se na připojení, Server v provozu")
"""Tady vytvoříme slovník s hrami ke kterým bude přiřazena unikátní ID aby jsme měli možnost většího(až neomezeného) 
počtu her a pokud hru hráč opustí budeme tuto hru mazat podle její ID"""

pripojeni = set() #uchová ip adresy připojených hráču
hry = {} #v tomto slovníku budeme mít naše hry s příslušnou ID
idPocitani = 0

"""Tady řesíme počítání hráču kteří jsou připojeni a rozdělujeme hráče na hráče 1 a 2 dále rozlišujeme
 přijatá data na reset hry, get nebo na tah, a mažeme hru podle ID"""

def threaded_klient(conn,p,hraId):
	global idPocitani#aby jsme věděli stále kolik hráču je připojeno
	conn.send(str.encode(str(p))) #odešle zprávu jestli jsme hráč 1 nebo 2

	reply = ""
	while True:
		try:
			data = conn.recv(4096).decode() #4096 protože tam mohou být větší informace; neustále dostáváme  data jestli hra ještě běží
			#kontorluje jestli je hra platná(oba hráči jsou tam)
			if hraId in hry:
				hra=hry[hraId]

				if not data:
					break
				else:
					if data == "reset":
						hra.resetWent()
					elif data != "get": #pokud nejsou data reset ani get musí to být tah
						hra.hrat(p,data)

					conn.sendall(pickle.dumps(hra)) #celou hru nám to přeloží do binární formy

			else:
				break
		except: #pokud by server neběžel správně
			break

	print("Ztráta Spojení")
	try:
		del hry[hraId] #smažeme hru podle ID, try proto protože pokud opustí hru oba zaroveň smaže se sama
		print("Vypinám Hru",hraId)
	except:
		pass
	idPocitani -= 1
	conn.close()

"""zatímco běží server  počítáme kolik máme hráču na serveru(přičítáme připojené) a pokud se připojí lichý hráč vytvoříme novou hru """

while True:
	conn, adresa = s.accept()
	print("Připojen k :", adresa)

	idPocitani +=1 #počítá kolik máme hráču
	p =0
	hraId = (idPocitani-1)//2 # hlídá nám aby na každou hru byli dva hráči 
	if idPocitani % 2 ==1 : #pokud se připojí lichý hráč musíme vytvořit novou hru
		hry[hraId] = Hra(hraId)
		print("Vytvářím novou hru")
	else: #sudý hráč se připojí do již vytvořené hry
		hry[hraId].ready = True
		p=1

	start_new_thread(threaded_klient, (conn,p,hraId))