import random
class ForceWielder:
    def __init__(self,name):
        self.name = name
        self.power = random.randint(1,15)
        self.wisdom = random.randint(1,15)



    def train(self):
        pass


    def fight(self,person):
       power1= self.power*self.wisdom/self.power+self.wisdom
       power2= person.power*person.wisdom/person.power+person.wisdom
       if  power1 > power2:
        print(f"{self.name} uses a {self.lightsaber_color} lightsaber and wins with an attack that took {power1}points from {person.name} used {person.lightsaber_color} lightsaber and was defeated had {power2}")
        return True
       else:
           print(f"{person.name} wins with a {person.lightsaber_color} lightsaber the attack was {power2} points {self.name}'s {self.lightsaber_color}lightsaber had {power1}")
           return False

    def is_jedi(self):
        pass

class Jedi(ForceWielder):
    def __init__(self,name):
        super().__init__(name)
        self.power = random.randint(1,15)
        self.wisdom =random.randint(1,15)+ 10
        if self.wisdom > self.power:
            self.lightsaber_color = "green"
        elif self.wisdom < self.power:
            self.lightsaber_color = 'blue'
        elif self.wisdom == self.power:
            self.lightsaber_color = 'purple'

        def train(self):
            self.power + random.randint(5, 15)
            self.wisdom + random.randint(10, 20)

        def is_jedi(self):
            return True


class Sith(ForceWielder):
    def __init__(self,name):
        super().__init__(name)
        self.name = "Darth " + name
        self.lightsaber_color = 'Red'
        self.power = random.randint(1,15)+10
        self.wisdom =random.randint(1,15)


    def train(self):
        self.power+ random.randint(10,20)
        self.wisdom+ random.randint(5,15)

    def is_jedi(self):
        return False








