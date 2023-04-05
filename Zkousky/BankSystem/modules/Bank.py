from .Transaction import Date, Transaction
from .Account import Account

class Bank:
    path:str
    transactions: list[Transaction]
    
    def __init__(self, path:str) -> None:
        self.path = path
        with open(path,'r') as f:
            self.transactions = [Transaction(l) for l in f.read().split('\n')]
        self.transactions.sort()
    
    def getAccount(self,account: int):
        return Account(account,self)
    
    def createTransaction(self,fr :int, to: int, amount: int, date: Date):
        if Account(fr,self).balance>=amount and fr!=to:
            self.transactions.append(Transaction(fr=fr, to=to, amount=amount, date=date))
            self.transactions.sort()
        else:
            print("Transaction not possible")
    
    def getAccountTransactions(self, account:int)->list[Transaction]:
        return [t for t in self.transactions if t.isConectedToAccount(account)]
            
    def __del__(self)->None:
        with open(self.path,'w') as f:
            out:str=""
            for t in self.transactions:
                out+=t.__repr__()+'\n'
            f.write(out)
    
    def __repr__(self) -> str:
        out:str = ""
        for t in self.transactions:
            out+=t.__repr__()+'\n'
        return out