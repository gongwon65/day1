#1

class Person:
    def __init__(self, name ,age ):
        self.name = name
        self.age = age
    
    def greet(self):
        return f'{self.name}님이 {self.age}살입니다'
person1 = Person("홍길동", 30)
print(person1.greet())


#2
class BankAccount:
    def __init__(self, account_number, balace=0):
        self.account_number = account_number
        self.balance = balace
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance < amount:
            print('잔액이 부족합니다다')
        else:
            self.balance -= amount
    
    def tranfer(self, amount, target_account):
        if self.balance < amount:
            print('잔액이 부족합니다')
        else:
            self.withdraw(amount)
            target_account.deposit(amount)

account1 = BankAccount(12345, 1000)
account2 = BankAccount(67890, 500)

account1.tranfer(100, account2)

print(account1.balance)
print(account2.balance)

#3
