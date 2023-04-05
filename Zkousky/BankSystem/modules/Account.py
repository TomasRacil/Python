from .Transaction import Date, Transaction

class Account:
    account: int
    balance: int
    bank=None
    transactions: list[Transaction]
    
    def __init__(self, account:int, bank) -> None:
        self.account=account
        self.bank = bank
        self.updateTransactions()
    
    def calculateBalance(self)->None:
        self.balance = sum([t.amount if t.isIncoming(self.account) else -(t.amount) for t in self.transactions])
        
    def makePayment(self, to: int, amount: int, date: Date):
        self.bank.createTransaction(self.account, to, amount, date)
    
    def updateTransactions(self)->None:
        self.transactions=self.bank.getAccountTransactions(self.account)
        self.calculateBalance() 
        
    def showTransactionBefore(self, date: Date)->None:
        print(f"Transactions before: {date.__repr__()}")
        print('\n'.join([t.__repr__() for t in self.transactions if (t.date<date)]),'\n')
        
    
    def showTransactionAfter(self, date: Date)->None:
        print(f"Transactions after: {date.__repr__()}")
        print('\n'.join([t.__repr__() for t in self.transactions if not(t.date<date)]),'\n')
        
    def __repr__(self) -> str:
        self.updateTransactions()
        out:str =f"Account: {self.account}\nBalance: {self.balance}\n"
        for t in self.transactions:
            out+=t.__repr__()+'\n'
        return out
    