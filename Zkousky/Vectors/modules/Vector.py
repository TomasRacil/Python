from __future__ import annotations
from math import sqrt

class Vector:
    def __init__(self,name:str,x:float,y:float,z:float) -> None:
        self.name=name;
        self.x = x;
        self.y = y;
        self.z = z;
    def sum(self, obj: Vector)->Vector:
        return Vector(
            self.name+" + "+obj.name,
            self.x+obj.x,
            self.y+obj.y,
            self.z+obj.z
            )
    def diff(self, obj: Vector)->Vector:
        return Vector(
            self.name+" - "+obj.name,
            self.x-obj.x,
            self.y-obj.y,
            self.z-obj.z
            )
    def vect_mult(self, obj: Vector)->Vector:
        return Vector(
            self.name+" x "+obj.name,
            self.y * obj.z - self.z * obj.y,
            self.z * obj.x - self.x * obj.z,
            self.x * obj.y - self.y * obj.x
            )
    def scal_mult(self, scl: float)->Vector:
        return Vector(
            self.name+" * "+str(scl),
            self.x * scl,
            self.y * scl,
            self.z * scl
            )
    def vector_size(self)->float:
        return sqrt(self.x*self.x+self.y*self.y+self.z*self.z)
    def __repr__(self) -> str:
        return f"Vektor {self.name} ({self.x}, {self.y}, {self.z}) |{self.name}|={self.vector_size()}\n"