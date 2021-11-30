class Waypoint:
	positionEast=10
	positionNorth=1

	def rotate(self,direction,value):
		if value==180:
			self.positionEast,self.positionNorth=-self.positionEast,-self.positionNorth
		elif value==90 and direction=="L" or value==270 and direction=="R":
			self.positionEast,self.positionNorth=-self.positionNorth,self.positionEast
		elif value==270 and direction=="L" or value==90 and direction=="R":
			self.positionEast,self.positionNorth=self.positionNorth,-self.positionEast

	def move(self, direction ,value):
		if direction == "N": self.positionNorth+=value
		elif direction == "E": self.positionEast+=value
		elif direction == "S": self.positionNorth-=value
		elif direction == "W": self.positionEast-=value

	def get(self):
		return self.positionEast,self.positionNorth

class Ship:
	positionEast=0
	positionNorth=0
	def __init__(self,waypoint,navigation):
		self.waypoint=waypoint
		self.navigation=navigation

	def move(self,value):
		self.positionEast+=waypoint.positionEast*value
		self.positionNorth+=waypoint.positionNorth*value

	def navigate(self):
		for command,value in navigation:
			if command=="L" or command=="R": waypoint.rotate(command,value)
			elif command=="F": self.move(value)
			else: waypoint.move(command,value)

	def info(self):
		print(self.positionEast,self.positionNorth)

navigation=[[line.strip()[0],int(line.strip()[1:])] for line in open("navigation.txt", "r")]

waypoint=Waypoint()
ship=Ship(waypoint,navigation)

ship.navigate()
ship.info()
		