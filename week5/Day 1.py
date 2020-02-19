import math

# class House:
#     def __init__(self,  city, num_rooms, landlord, rent):
#         self.city = city
#         self.num_rooms = num_rooms
#         self.landlord =landlord
#         self.rent = 1000 * self.num_rooms
#         if city = "TA":
#             rent *= 2
#
#         def sign_contract(self, name, date):
#             if self.landlord = "Moti":
#                 self.rent *= 2
#                 print(f"Rental agreement between {name} and {self.landlord}")
#         def complain_about_broken_window(self):
#             print(f"{self.landlord} says ")
#
# class Dog:
#     def __init__(self,name,color,type,sound,height):
#         self.name = name
#         self.color = color
#         self.type = type
#         self.sound = sound
#         self.height = height
#         self.jump = 2 * self.height
#
#     def talk (self):
#         print(f"{self.name} said {self.sound}")
#
#
#
# davids_dog = Dog("Rex","brown","pitbull","woof",50)

# class Zoo:
#     def __init__(self, name):
#         self.animals = []
#         self.name = name
#
#     def addAnimals(self, newAnimal):
#         if newAnimal not in self.animals:
#             self.animals.append(newAnimal)
#
#     def getAnimals(self,name):
#         print(f"the animals in {self.name} are {self.animals}")
#
#     def sellAnimal(self,animalName):
#         animalName = input("which animal are you selling?")
#         if animalName in self.animals:
#             self.animals.remove(animalName)
#             print(f"goodbye {animalName}")
#             print(f"These are now the animals in {self.name} ,{self.animals}")
#
#     def sortAnimal(self,x):
#         sorted_animals = sorted(self.animals)
#         print(sorted_animals)
#         y = slice(input("enter the first letter of your animal"))
#         temp = 0
#         new_pen = []
#         for x,y in zip(self.animals[::],self.animals[1::]):
#             print(self.animals[1::])
#             if x[0] == y[1]:
#                 new_pen[temp] = [x,y]
#                 new_pen.append(zip(sorted_animals))
#             else:
#                 temp += 1
#         return print(zip(sorted_animals))
#
#
# jzoo = Zoo("jayszoo")
# jzoo.addAnimals("monkey")
# jzoo.addAnimals("fox")
# jzoo.addAnimals("baboon")
# jzoo.addAnimals("bear")
# jzoo.addAnimals("fly")
# jzoo.addAnimals("mudpig")
# jzoo.addAnimals("horse")
# print(jzoo.animals[:temp:])
# # jzoo.getAnimals(jzoo)
# jzoo.sortAnimal("")


class Circle:
    def __init__(self,radius):
        self.radius = radius

        def area(self):
            return math.pi == self.radius**2
        @staticmethod
        def compute_are(r):
            return math.pi * r ** 2

        if __name__ == '__main__':
            c = circle(radius=2)
            print(c.area())
            print(c.compute_area(r=5))