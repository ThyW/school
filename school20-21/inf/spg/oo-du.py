#!/usr/bin/python3
import random

MAX = 3 
MAX_BANK_ACCS = 20000000000

class Bank:
    def __init__(self):
        self.accounts = list()
        self.used_ids = list()
        self.used_names = list()

    def generate_id(self):
        id1 = random.randint(0, MAX_BANK_ACCS)
        while id1 in self.used_ids:
            id1 = random.randint(0, MAX_BANK_ACCS)
        self.used_ids.append(id1)
        return id1
    
    def get_account(self, id):
        for i in self.accounts:
            if i.get_id() == id:
                return i

    def add_acc(self, user, passwd, balance):
        acc = Account(user, passwd, balance)
        id1 = self.generate_id()
        acc.set_id(id1)
        self.accounts.append(acc)

    def exists(self, user):
        for acc in self.accounts:
            if acc.get_user() == user:
                print("account with id: " + acc.get_id() + "and username: " + acc.user)
                return
        print("no such account")

   
    def login(self, user, passwd):
        for acc in self.accounts:
            if acc.get_user() == user:
                if acc.get_passwd() == passwd:
                    print("logged in")
                    acc.logged = True
                    return 
                else:
                    if MAX >= acc.att:
                        if acc.att == 0:
                            print("max attempts reached, account is blocked")
                            acc.blocked = True
                            return
                        acc.att -= 1
                        print("wrong attempt; " + str(acc.att) + " attempts remain")
                        return
    
    def withdraw(self, user, amount):
        for acc in self.accounts:
            if acc.get_user() == user:
                if acc.blocked == False and acc.logged == True:
                    if acc.balance >= amount:
                        acc.balance -= amount
                        print("Withdrawn successfully")
                        return
                    else:
                        print("Not enough money on the account")
                        return
                elif acc.blocked == True:
                    print("Unable to withdraw, account blocked")
                    return
                elif acc.logged == False:
                    print("Login first, please")
                    return
        print("No such account in our bank")

    def deposit(self, user, amount):
        for acc in self.accounts:
            if acc.get_user() == user:
                if acc.blocked == False and acc.logged == True:
                    acc.balance += amount
                    print("Deposited successfully")
                    return 
                elif acc.blocked == True:
                    print("Unable to deposit, account blocked")
                    return
                elif acc.logged == False:
                    print("Login first, please")
                    return
        print("No such account in our bank")

    def balance(self, user):
        for acc in self.accounts:
            if acc.user == user: 
                if acc.blocked == False and acc.logged == True:
                    return acc.balance
                elif acc.blocked == True:
                    print("Unable to deposit, account blocked")
                    return
                elif acc.logged == False:
                    print("Login first, please")
                    return
        print("n such account")

    def get_id(self, user):
        for acc in self.accounts:
            if acc.user == user:
                print(acc.get_id())
                return acc.get_id()
        print("No such account")


class Account: 
    def __init__(self, user, passwd, balance):
        self.__user = user
        self.__passwd = passwd
        self.__balance = balance
        self.__id = -1
        self.logged = False
        self.blocked = False
        self.att = MAX
    
    def get_balance(self):
        return self.__balance
    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id
    def set_balance(self, amount): 
        self.__balance = amount
    def get_password(self):
        return self.__passwd
    def set_password(self, passwd):
        self.__passwd = passwd
    def get_user(self):
        return self.__user
    def set_user(self, user):
        self.__user = user

def main():
    bank = Bank()

    # works!
    bank.add_acc("jozkok", "heslo", 15)
    bank.login("jozkok", "heslo")
    bank.deposit("jozkok", 53)
    bank.withdraw("jozkok", 50)

    # login atttempts demonstration
    bank.add_acc("fero", "12", 0)
    bank.login("fero", "13")
    bank.login("fero", "13")
    bank.login("fero", "13")
    bank.login("fero", "13")

if __name__ == "__main__":
    main()

