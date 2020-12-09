#! /usr/bin/python3 
import random
class Mammal:
    def __init__(self, name, age, sex): 
        self.__name = name
        self.__age = age
        self._sex = sex
    
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_sex(self):
        if self._sex == True:
            return True
        if self._sex == False:
            return False

    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        self.__age = age

    def mammal_sound(self):
        return "Some sound idk lmao"
    def mammal_movement(self):
        return "moving an arbitrary amount of steps"

class Dog(Mammal):
    def __init__(self, name, age, sex, breed, hair_color):
        super().__init__(name, age, sex)
        self.__breed = breed
        self.__hair_color = hair_color

    def get_breed(self):
        return self.__breed

    def get_hair_color(self):
        return self.__hair_color

    def set_breed(self, breed):
        self.__breed = breed

    def set_hair_color(self, hair_color):
        self.__breed = hair_color

    def breed_with(self, dog: 'Dog'):
        if self.get_sex() != dog.get_sex():
            return Dog("", 0, random.choice((True, False)), random.choice((self.__breed, dog.get_breed)), random.choice((self.__hair_color, dog.get_hair_color())))


class Cat(Mammal):
    def __init__(self):
        self.__age = 15

d1 = Dog("jozo", 14, True, "husky", "pink")
print(d1.get_age())

d2 = Dog("ala", 12, False, "terier", "red")
d3 = d1.breed_with(d2)
print(str(d3.get_sex()) + d3.get_hair_color())
