class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        return f'{self.name}님이 {self.age}살입니다'
        
person1 = Person('홍길동', 30)
print(person1.greet())




class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.amount = amount
        self.balance += amount
        print (f'계좌에 {amount}원을 입금합니다.')
        print (f'현재 잔액{self.balance}원 입니다.')

    def withdraw(self, amount):
        self.amount = amount
        if amount > self.balance:
            print (f'계좌에서 {amount}원을 출금합니다.')
            print ('잔액이 부족합니다')
            print (f'보유 금액은 {self.balance}원 입니다.')
        else:
            self.balance -= amount
            print (f'계좌에서 {amount}원을 출금합니다.')
            print (f'남은 잔액 {self.balance}원 입니다.')


           
account1 = BankAccount(12345, 1000)
account1.deposit(500)
account1.withdraw(200)
account1.withdraw(2000)