from __future__ import annotations

class Date:
    day: int
    month: int
    year: int
    
    def __init__(self, day:int, month:int, year:int) -> None:
        self.day = day
        self.month = month
        self.year = year
        
    def __lt__(self, other: Date)->bool:
        if self.year<other.year:return True
        elif self.year>other.year: return False
        else:
            if self.month<other.month:return True
            elif self.month>other.month: return False
            else:
                if self.day<other.day:return True
                else:return False
    def __repr__(self)->str:
        return f"{self.day}.{self.month}.{self.year}"