class Account:

    name = ""
    balance = 0
    def __init__(self , name):
        self.name = name

    def deposit(self , a):
        self.balance += a

    def withdraw(self , a):
        if a > self.balance:
            print("You don't have enough money")
        else:
            self.balance -= a
            print("Success ! ,You have" , self.balance)




chel = Account("Talga")

chel.deposit(1000000)
chel.withdraw(50000)
