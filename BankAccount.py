class BankAccount:

    def __init__(self,accountNumber, name,balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def Deposit(self,amount):
        self.balance+=amount

    def Withdrawal(self,amount):
        if(self.balance < amount):
            print("Impossible to withdraw from this account")
        self.balance-=amount

    def bankFees(self):
        self.balance-=self.balance*0.05


    def display(self):
        print(self.accountNumber +" "+ self.name + " " + str(self.balance))




user = BankAccount("3165268900","Jay",50000)
user.display()
user.Deposit(37800)
user.Withdrawal(7800)
user.display()
user.bankFees()
user.display()

users = []
users.append(BankAccount("111","Yoni",800))
users.append(BankAccount("111","Yonas",900))
users.append(BankAccount("111","Yonis",8700))
users  .append(BankAccount("111","Yonix",700))
for user in users:
    user.display()

print(users[-3].display()) #negative indexing
#https://www.geeksforgeeks.org/python-list-slicing/ slicing fundamentals
miniusers = users[2:4]
for mi in miniusers:
    mi.display()