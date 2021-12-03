class Ship:
	orientation=90
	positionE=0
	positionS=0

	def move(self, direction ,value):
		if direction == "F": 
			if self.orientation==0:self.positionS-=value
			elif self.orientation==90:self.positionE+=value
			elif self.orientation==180:self.positionS+=value
			elif self.orientation==270:self.positionE-=value
		elif direction == "N": self.positionS-=value
		elif direction == "E": self.positionE+=value
		elif direction == "S": self.positionS+=value
		elif direction == "W": self.positionE-=value

	def turn(self, direction, value):
		if direction=="L": self.orientation = self.orientation-value + (360 if self.orientation-value<0 else 0)
		elif direction=="R": self.orientation = self.orientation+value - (0 if self.orientation+value<360 else 360)

	def degreesToOrientation(self,degree):
		return {0:"N",90:"E",180:"S",270:"W"}[degree]

	def orientationTodegrees(self,orientation):
		return {"N":0,"E":90,"S":180,"W":270}[orientation]

	def info(self):
		print(self.orientation,self.positionE,self.positionS)

	def navigate(self, navigation):
		for command,value in navigation:
			if command=="L" or command=="R": self.turn(command,value)
			else: self.move(command,value)

	def showNavigation(navigation):
		for line in navigation: print(line)


navigation=[[line.strip()[0],int(line.strip()[1:])] for line in open("navigation.txt", "r")]

ship=Ship()
ship.navigate(navigation)
ship.info()
