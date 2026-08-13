class BankAccount:
    # by default class has public attribute
    def __init__(self,name,balance):
        self.name = name
    # self._balance = balance #protected
        self.__balance = balance #private

    def get_balance(self): #getter
        print(self.__balance) 
    
    def deposit(self , deposit): #setter
        if deposit > 0:
            self.__balance += deposit
            print(self.__balance)
        else:
            print("Invalid deposit")
    
    def withdrawl(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
            else:
                print("Insufficient balance")
        else:
            print("Invalid deposit")

acc1 = BankAccount("parmarth" , 10000)
print(acc1.name)
acc1.deposit(-1100)

acc1.get_balance
acc1.deposit(1100)
acc1.get_balance
acc1.withdrawl(5000)
acc1.get_balance

try:
    print(acc1.__balance)
except Exception as e:
    print(f"Cant access private data. [{e}]")


print(acc1._BankAccount__balance)
