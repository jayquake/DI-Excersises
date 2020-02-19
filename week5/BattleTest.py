from Starwars import Jedi,Sith
import random

jay = Jedi(f"Jason")
obi = Jedi("Obi")
print(obi.lightsaber_color)
luke = Jedi("Luke")
vader = Sith("Vader")
asshole = Sith("Asshole")
maul = Sith("Maul")
jay.fight(asshole)
jedis = [jay, obi, luke]
siths = [vader, maul,asshole]

print(jedis)
print(siths)
fights = 0
while siths:
    jedi = random.choice(jedis)
    sith = random.choice(siths)
    if sith.fight(jedi):
        sith.train()
    else:
        siths.remove(sith)
    jedi.train()
    fights += 1

print(fights)