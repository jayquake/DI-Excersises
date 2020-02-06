import random
#
# def talk():
#     p= random.random()
#     if p > 0.5:
#         return "whatever"
#
#     else:
#         print("coin toss")
#         return "sometheing else"

# def multiply(num, multiplier =2):
#     return num * multiplier
#
# # output = multiply(10,5)
# # print(output)
#
# nul =[multiply(2, multiplier) for multiplier in range (1,11)]
# print(nul)
#

# person = "jason"
#
# def say_name(person):
#     person += "something"
#
#     say_name(person)
#     print("hey {} ".format(person))

# def show_names(*args):
#     for i,name in enumerate(args):
#         print(f"person number {i}: {name}")
#
# show_names('yair', 'shlomo','rachel','eran','eli')

# def show_info(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
#
# info = {"name": "fred", "last name": "monkey", "profession":"philpsopher", "nationality": "german"}
#
# show_info(name='fred',lastname='monkey', profession='philosopher',nationality='german')

# current_date =2020,5
# Year = 2020
# Month = 2
# def get_age(year:int,month:int,day:int):
#     if month >= Month:
#         age = Year -year -1
#     else:
#         age = Year - year
#     return age
#
#
# print(1988,12,2)
#
# def can_retire(sex,date_of_birth):
#     args = list(map(int,date_of_birth.split('/')))
#     month, day,year = args[0],args[1], args[2]
#     age = get_age(year,month,day)
#     print(f'your age us{age}')
#     if sex == "Male":
#         if age >= 67:
#             return True
#         else:
#             return age >= 62
#         print(can_retire("Female","1/5/1990"))
#
# def get_temp(season):
#     temp = random.randint(-10 , 40)
#
#     winter = random.randint(-10, 16)
#     spring = random.randint(24, 31)
#     summer = random.randint(32,40)
#     fall = random.randint(17,23)
#     season= winter, spring,summer,fall
#     if season.lower() == 'summer':
#         temp = summer
#     elif season.lower() == 'spring':
#         temp = spring
#     elif season.lower() == 'fall':
#         temp = fall
#     elif season.lower() == 'winter':
#         temp = winter
#     return temp
#
#
# def main(*arg):
#     season= input("what season is it")
#     temp = get_temp(season)
#     if get_temp() >= 20 or get_temp() <= 30:
#         return ("Its pretty nice out")
#     elif get_temp() >=10  or get_temp() <= 19:
#         return ("its a bit chilly")
#     elif get_temp() >= 31 or get_temp() <= 40:
#         return ("youre gonna sweat")
#     else:
#         return ("its  bloody cold")
#
# print(main())

def throw_dice (*args):
    args = random.randint(1,6)
    return args



def throw_until_doubles():
    die1 = throw_dice()
    die2 = throw_dice()
    counter = 1
    while die1 != die2:
        counter += 1
        print(die1, die2)
        die1 = throw_dice()
        die2 = throw_dice()
        print(die1,die2)
    return counter
#


def main():
    die1 = throw_dice()
    die2 = throw_dice()
    counter = 1
    counter2 = 1
    print(die1,die2)
    while counter != 100:
        if die1 == die2:
            counter += 1
        print(die1,die2)
        die1 = throw_dice()
        die2 = throw_dice()
        counter2 += 1
        print(counter)
        print (f"It took {counter2} throws to complete 100 doubles ")
        print(f" it takes an average of {counter2//counter} throws to get a double")
print(main())

# firstname = input("whats your first name ")
# middlename = input("whats your middle name")
# lastname = input("whats your last name")
# def get_full_name():
#     full_name = firstname+middlename+lastname
#     return (f"Your full name is {full_name}")
#
# print(get_full_name())