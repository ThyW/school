#!/usr/bin/python3

class Rect: 
    def __init__(self, width, height): 
        self.width: int= width
        self.height: int = height

    def area(self):
        area = self.width * self.height
        return area

    def obvod(self):
        circ = (2 * self.width) * (2 * self.height) # aaaa
        return circ
    
class Mammal:
    def __init__(self, a, w, n): 
        self.age: int = a
        self.weight: int = w
        self.name: str = n

    def movement(self):
        print(self.name + " is moving")


opica = Mammal(3, 5, "jozo")
slon = Mammal(213, 5000, "dumbo")
print(opica.age)
print(opica.weight)
print(opica.name)

opica.movement()
slon.movement()

#
#
#

class Bank:
    def __init__(self):
        self.current = 0
        self.id_list = list()
        self.accounts = {}
        for i in range(0, 1024):
            self.id_list.append(i)

    def insert(self, acc):
        c = self.id_list[self.current]
        self.accounts[c] = acc
        self.current += 1

    def get(self, user):
        for acc in self.accounts.values():
            if str(acc.user) == str(user):
                print(acc.user)
                ret = acc
            else:
                continue
        if not ret != None:
            return ret 
        else: 
            print("No such account")
        
class BA:
    def __init__(self, user, heslo):
        self.user = user
        self.__heslo = heslo
        self.stav = 0
        self.__attempts = 0
        self.__max = 3
        self.__logged = False
        print("Ucet otvoreny! Vitaj " + self.user) 

    def login(self, user, heslo):
        if self.user == user and self.__heslo:
            print("logged in")
        else:
            if self.__attempts < self.__max:
                self.__attempts += 1
                print("wrong: " + (self.__max - self.__attempts) + "attempts remaining")
                self.logged = True
            else:
                print("logged off, max number of failed attempts")

    def takeOut(self, amount):
        if self.logged == False:
            print("log in!")
            return
        else:
            if amount <= self.stav:
                self.stav -= amount
                print("your amount: " + self.stav)

            else: 
                print("not enough on the account")

    def putIn(self, amount):
        if self.logged == False:
            print("log in!")
        else: 
            self.stav += amount
            print("your amount is: " + self.stav)
            

def main():
    bank = Bank()

    acc1 = BA("acc1", "heslo1")
    print(acc1.user)
    acc2 = BA("acc2", "heslo2")
    acc3 = BA("acc3", "heslo3")

    bank.insert(acc1)
    bank.insert(acc2)
    bank.insert(acc3)
    
    bank.get("acc1").login("acc1", "heslo1").putIn(13)
    print(bank.get("acc1").stav)

if __name__ == "__main__":
    main()
