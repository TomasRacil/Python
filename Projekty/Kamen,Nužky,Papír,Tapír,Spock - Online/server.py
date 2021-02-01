import socket
from _thread import *
import pickle #umožnuje nám poslat objekt ve formě jedniček a nul a poslat ji přes internet a potom ji zpětně přeměnime na objekt
from hra import Hra

server = "192.168.14.214"
port = 5555
#nadefinujeme typy připojení(ipv4,TCP protocol)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#přiřadíme portu adresu
try:
	s.bind((server, port))
except socket.error as e:
	str(e)

s.listen(2) #omezení počtu hráču
print("Čeká se na připojení, Server v provozu")
# pokud chceme mít neomezený počet hráču musíme mít neomezený počet her v jednu chvíli, tak vytvoříme slovník s hrama
#hry budou přístupné s jejich ID kterou budou mít
pripojeni = set() #uchová ip adresy připojených hráču
hry = {} #v tomto slovníku budeme mít naše hry s příslušnou ID
idPocitani = 0

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