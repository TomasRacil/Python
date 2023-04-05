from modules import *

if __name__ =="__main__":
    d = Date(5,3,2023)
    print(d, '\n')
    t = Transaction("1;2;538;1.1.2023")
    print(t, '\n')
    b = Bank("bank.txt")
    print(b, '\n')
    a1 = b.getAccount(1)
    a2 = b.getAccount(2)
    print(a1,'\n',a2,'\n')
    a2.makePayment(1, 100, Date(7, 3, 2023));
    a1.makePayment(2, 10000, Date(7,3,2023));
    print(a1,'\n',a2,'\n')
    a1.showTransactionBefore(d)
    a1.showTransactionAfter(d)