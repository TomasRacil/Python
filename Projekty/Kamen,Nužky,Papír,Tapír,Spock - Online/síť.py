import socket
import pickle

class Sit:
	def __init__(self):
		self.klient = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #skrze protokol ipv4 a TCP
		self.server = "192.168.14.214" #ip počítače který vytvoří server
		self.port = 5555 #jakýkoliv volný otevřený port
		self.adresa = (self.server , self.port)
		self.p = self.connect()

	def ziskejP(self):
		return self.p

	def connect(self):
		try:
			self.klient.connect(self.adresa)
			return self.klient.recv(2048).decode() #hráč dostane číslo 1 nebo 2
		except:
			pass

	def send(self,data):
		try:
			self.klient.send(str.encode(data)) #posíláme na server stringové data
			return pickle.loads(self.klient.recv(2048*2)) # od serveru dostáváme binární pickle data
		except socket.error as e:
			print(e)