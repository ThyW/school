#!/usr/bin/env python3

import ll

# example of a simple hash function
# hash = sum(ascii(string)) % 100
def primitive_hash(string):
    sum = 0
    for c in string:
        sum += ord(c)

    return sum % 100

class HashTable:
    def __init__(self, hash_function):
        self.__data = [[]] * 100
        self.__data2 = [ll.LL()] * 100
        self.__hf = hash_function

    # insert a new key and value into the hash table
    def insert(self, key, val):
        self.__data[self.__hf(key)] = val

    def __str__(self):
        ret = ""

        for each in self.__data:
            if each:
                ret += f"{each[0]}\n" 
        return ret
    
    # get a value for a key from hash table
    def get(self, key):
        index = self.__hf(key)
        if self.__data[index]:
            return self.__data[index]

    # if there already is an entry for the given hash, insert the data to the next free space in our list
    def insert_linear(self, key, val):
        index = self.__hf(key)

        while self.__data[index]:
            index += 1

        self.__data[index] = val
    
    # this is pretty dumb, defeats the whole purpose of Hash Tables
    # :/
    def get_linear(self, key, val):
        index = self.__hf(key)

        while self.__data[index]:
            if self.__data[index] == val:
                return self.__data[index]
            
            index += 1

    def insert_ll(self, key, val):
        index = self.__hf(key)

        self.__data2[index].push_back(val)

    def get_ll(self, key, val):
        index = self.__hf(key)

        if self.__data2[index].get(val):
            return val

        return None

def test():
    hm = HashTable(primitive_hash)

    hm.insert("jozko", "j")
    hm.insert("ferko", "f")
    hm.insert("maria", "m")
    
    try:
        assert hm.get("maria") == "m"
    except:
        print("test: failed")
test()

def test2():
    hm = HashTable(primitive_hash)

    hm.insert_linear("asd", "a")
    hm.insert_linear("dsa", "b")
    
    try:
        assert hm.get_linear("dsa", "a") == "a"
    except:
        print("test2: failed")
test2()

def test3():
    hm= HashTable(primitive_hash) 

    hm.insert_ll("asd", "a")
    hm.insert_ll("sda", "b")

    try:
        assert hm.get_ll("sda", "b") == "b"
    except:
        print("test3: failed")
