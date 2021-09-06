#!/usr/bin/env python3

data = [[]] * 100

# example of a simple hash function
# hash = sum(ascii(string)) % 8
def primitive_hash(string):
    sum = 0
    for c in string:
        sum += ord(c)

    return sum % 100

class HashMap:
    def __init__(self, hash_function):
        self.__data = [[]] * 100
        self.__hf = hash_function

    def insert(self, key, val):
        self.__data[self.__hf(key)] = val

    def __str__(self):
        ret = ""

        for each in self.__data:
            if each:
                ret += f"{each[0]}\n" 
        return ret

    def get(self, key):
        index = self.__hf(key)
        if self.__data[index]:
            return self.__data[index]


def test():
    hm = HashMap(primitive_hash)

    hm.insert("jozko", "j")
    hm.insert("ferko", "f")
    hm.insert("maria", "m")
    
    if hm.get("ferko") == "f":
        print("test: passed")
    else:
        print("test: failed")

test()
