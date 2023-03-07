from __future__ import annotations

from .Vector import Vector

class VectorGroup:
    def __init__(self, path: str) -> None:
        with open(path, "r", encoding="utf_8") as file:
            self.vectors = [
                Vector(
                    line.split(';')[0],
                    float(line.split(';')[1]),
                    float(line.split(';')[2]),
                    float(line.split(';')[3]),
                    ) for line in file.read().split("\n")]
            self.vectors.sort(key=lambda x: x.vector_size())
    
    def add_vector(self, vector: Vector) -> None:
        self.vectors.append(vector)
        self.vectors.sort(key=lambda x: x.vector_size())
        
    def get_vector(self, name:str) -> Vector:
        for v in self.vectors:
            if v.name == name:
                return v
            
        return None
        
    def sum_vectors(self)->Vector:
        s = Vector("0",0,0,0)
        for v in self.vectors:
            s = s.sum(v)
        return s
    
    def __repr__(self) -> str:
        out=""
        for v in self.vectors:
            out+=v.__repr__()
        return out