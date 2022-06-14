from math import sqrt

class Beacon:
    map=[]
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    
    def calculateDistances(self,beacons):
        beacons.remove(self)
        self.map=[sqrt((self.x-beacon.x)**2+(self.y-beacon.y)**2+(self.z-beacon.z)**2) for beacon in beacons]

class Scaner:
    def __init__(self,data):
        self.name=data.pop(0)
        self.beacons=[Beacon(int(line.split(",")[0]),int(line.split(",")[1]),int(line.split(",")[2])) for line in data]
    
    def compareBeacons(self,scaner):
        for beacon in self.beacons:
            for beacon1 in scaner.beacons:
                input(beacon.__dict__)
                input(beacon1.__dict__)
                # input(set(beacon.map).intersection(set(beacon1.map)))

scaners=[]
with open(r"C:\Vyuka\Python\Zaklady\Scripty\AdventOfCode\2021\Racil\19\test.txt","r") as f:
    scaners=[Scaner(scaner.split("\n")) for scaner in f.read().split("\n\n")]


for scaner in scaners:
    #print(scaner.name)
    for beacon in scaner.beacons:
        beacon.calculateDistances(scaner.beacons)
        #input(sorted(beacon.map))

for scaner in scaners:
    for scaner1 in scaners:
        scaner.compareBeacons(scaner1)
