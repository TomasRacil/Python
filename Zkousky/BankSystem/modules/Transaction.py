from __future__ import annotations
from .Date import Date

class Transaction:
    fr: int
    to: int
    amount: int
    date: Date
    
    def __init__(self, transaction: str = '', fr:int=0, to:int=0, amount:int=0,date:Date=Date(0,0,0)) -> None:
        if transaction!='':
            temp=transaction.split(';')
            self.fr = int(temp[0])
            self.to = int(temp[1])
            self.amount = int(temp[2])
            self.date = Date(*[int(v) for v in temp[3].split('.')])
        else:
            self.fr = fr
            self.to = to
            self.amount = amount
            self.date = date
    
    def isConectedToAccount(self, account:int) -> bool:
        if self.fr == account or self.to == account:
            return True
        return False
    def isIncoming(self,account:int)->bool:
        if self.to == account:
            return True
        return False
    def __lt__(self, other: Transaction)->bool:
        if self.date<other.date:
            return True
        return False
    def __repr__(self) -> str:
        return f"{self.fr};{self.to};{self.amount};{self.date.__repr__()}"