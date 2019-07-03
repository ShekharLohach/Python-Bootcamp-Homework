class Account():

    def __init__(self,owner,balance=0):
        self.balance=balance
        self.owner=owner

    def __str__(self):
        return ("Account owner : {} Account balance : {}".format(self.owner,self.balance))


    def add(self,amount):
        self.balance=self.balance+amount
        print("your new balance is {}".format(self.balance))
    def withraw(self,amount):
            if(self.balance>=amount):
                print("balance is debited")
                self.balance=self.balance-amount
                print("your new balance is {}".format(self.balance))
            else:
                print("Insufficient Funds")

account=Account('shekhar',50)
print(account)
# account.add(700)
# account.withraw(700)
