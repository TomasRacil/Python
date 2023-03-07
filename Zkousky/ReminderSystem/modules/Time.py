from __future__ import annotations

class Time:
    year: int
    month: int
    day: int
    hour: int
    minute: int
    
    def __init__(self, time:str) -> None:
        t = time.split(" ")
        self.year = int(t[0])
        self.month = int(t[1])
        self.day = int(t[2])
        self.hour = int(t[3])
        self.minute = int(t[4])
        
    def __lt__(self, other:Time)->bool:
        if self.year<other.year:return True
        elif self.year>other.year: return False
        else:
            if self.month<other.month:return True
            elif self.month>other.month: return False
            else:
                if self.day<other.day:return True
                elif self.day>other.day: return False
                else:
                    if self.hour<other.hour:return True
                    elif self.hour>other.hour: return False
                    else:
                        if self.minute<other.minute:return True
                        elif self.minute>other.minute: return False
        return False
            
    
    def __eq__(self, other:Time)->bool:
        if (self.year==other.year 
            and self.month==other.month 
            and self.day==other.day
            and self.hour==other.hour
            and self.minute==other.minute): return True
        return False
        
    def __repr__(self) -> str:
        return f"{self.year}-{self.month}-{self.day} {self.hour}:{self.minute}"