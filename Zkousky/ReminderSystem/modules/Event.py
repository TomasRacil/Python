from __future__ import annotations

from .Time import Time

class Event:
    name:str
    start_time:Time
    end_time:Time
    place: str
    description: str
    
    def __init__(self, event:str) -> None:
        e = event.split("\n")
        self.name = e[0]
        self.start_time = Time(e[1])
        self.end_time = Time(e[2])
        self.place = e[3]
        self.description = e[4]
        
    def __lt__(self, other:Event) -> bool:
        if self.start_time<other.start_time: return True
        return False
    
    def __eq__(self, other:Event)-> bool:
        if (self.name==other.name 
            and self.start_time==other.start_time 
            and self.end_time == other.end_time
            and self.place == other.place): return True
        return False
    
    def __repr__(self) -> str:
        return f"""Name: {self.name}
Start: {self.start_time}
End: {self.end_time}
Place: {self.place}
Description: {self.description}"""