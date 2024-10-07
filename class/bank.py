class accountant:

    def __init__(self,bal,acc):
        self.balance=bal
        self.account=acc
        print(bal,acc)
    def balance(self):
       pass
    def debit(self,amount):
        self.balance-=amount
        print("Rs",amount,"was debited")
        print("Total balance=",self.getbalace())
    def credit(self,amount):
        self.balance += amount
        print("Rs",amount,"was credited")
        print("Total balance=", self.getbalace())
    def getbalace(self):

        return self.balance
s1=accountant(10000,12345)
s1.debit(1000)
s1.credit(5000)
s1.debit(1000)

