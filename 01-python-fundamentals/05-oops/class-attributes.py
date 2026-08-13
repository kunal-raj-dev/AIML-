class Bank:
    # class attributes common property of every new instance
    branch = "SBI Jaipur"

    def __init__(self, name, accNo, accType):
        self.name = name
        self.accNo = accNo
        self.accType = accType

    
person1 = Bank("Tanish",456388344545,"saving")

print(f"{person1.name},{person1.accType} Account, Account Number : {person1.accNo} in Branch : {person1.branch}")