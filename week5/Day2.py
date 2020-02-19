import math
class Family:
    def __init__(self, lastname):
        self.lastname = lastname
        self.members = []

    def add_member(self, name, age, sex, is_child):
        member_info= {
            'name': name,
            'age':age,
            'sex': sex,
            'is_child': is_child
        }
        self.members.append(member_info)


    def is_18(self,age):
         for children in self.members:
             if age in children.values():
                 if children.get("age") >= 18:
                     print(f"{children.get('name')} is over the age of 18")

             else: print(f"{children.get('name')} is under the age of 18 their age is {children.get('age')}")



quaicoo = Family("Quaicoo")
quaicoo.add_member('Jason',30, 'Male', False)
quaicoo.add_member('Reut',30, 'Female', False)
quaicoo.add_member('Noname',0, '?', True)
quaicoo.add_member('Noname2',0, '?', True)
print(quaicoo.members)
print(quaicoo.is_18(30))
# class TheIncredibles(Family):
#     def family(self, name,age,sex,is_child,power, incredible_name):
#         member_info = {
#             'name': name,
#             'age': age,
#             'sex': sex,
#             'is_child': is_child,
#             'power': power,
#             'incredible name':incredible_name
#             }
#         self.members.append(member_info)
#
#     def use_power(self,**kwargs):
#         Male = "he"
#         for children in self.members:
#             if kwargs in children.values():
#                 if children.get("age") >= 18 :
#                     print(f"{children.get('name')} is over the age of 18")
#
#             elif children.get("age") <= 18:
#                 print(f"{children.get('name')} is {children.get('age')} they can not use the power of {children.get('power')} without parental supervision")
#             else:
#                 print(f"{children.get('name')} is {children.get('age')} and {children.get('incredible name')} could use the power of {children.get('power')}")
#
#
# theincredibles = TheIncredibles("Parr")
# theincredibles.family("Bob", 43 ,"Male",False,"Stregnth","Mr.Incredible")
# theincredibles.family("Helen", 40 ,"Female",False,"Elasticity","Elasta-Girl")
# theincredibles.family("Violet", 17 ,"Female",True,"Invisibility","None")
# theincredibles.family("Dash", 10 ,"Male",True,"Speed","None")
# theincredibles.family("Jack", 3 ,"Male",True,"Unknown","None")
# print(theincredibles.members)
# print(theincredibles.use_power())
#



#
#
# class Bank:
#     def __init__(self,bankname):
#         self.account_holders = []
#
#     def create_user(self, owner, balance, card_num, password):
#         users = {
#             'owner': owner,
#             'balance': balance,
#             'card_num':card_num,
#             'password':password
#         }
#         self.account_holders.append(users)
#
#     def get_user(self,name):
#         for dic in self.account_holders:
#            owner = dic.get("owner")
#            if owner == name:
#                 return dic
#
#
#     def deposit(self):
#         account = self.get_user(input("Which user are you looking for")).get('balance')
#         amount_deposited = int(input("How much are you depositing"))
#         total = (account + amount_deposited)
#         # updated_account = account.update([balance])
#         # account["balance"] += amount_deposited
#         return print(f"Your total is{total}")
#
#
# bank1 = Bank("My Bank")
# bank1.create_user("Jason", 1000, 123456, "monkey")
# bank1.create_user("mike", 900, 123456, "monkey")
# print(bank1.account_holders)
# bank1.get_user('mike')
# print(bank1.get_user('mike'))
# ()

# bank1.deposit("Jason",100)
#     def deposit(self):
#         balance = self.account_holders.get('balance') = 0
#         account = self.account_holder
#
#         total = self.balance + amount_deposited
#         temp = 0
#         if amount_deposited <= 0:
#             print("You can not deposit 0 or less. Do you want to withdraw?")
#
#         return print(f"{account} you have deposited {amount_deposited} your total is {total} dollars")
# Chase = Bank()
# user = Bank.create_user(Chase,"Jason",1000,12345,"monkey")
# user.deposit(100)


# Chase = Bank("Jason","Chase",10000)
# Chase.deposit()
#
# class Owner(Bank):
#     def __init__(self,account_holder,balance,owner,card_num,password):
#         super().__init__(account_holder,owner,balance)
#         self.card_num = card_num
#         self.password = password
#     def check_owner_info(self,card_num):
#         temp = 0
#         card_num = "12345"
#         # password = "monkey"
#         for num in card_num:
#             if num in card_num != card_num:
#                 temp += 1
#                 print("card number incorrect. Try again")
#                 if temp >= 2:
#                     print("Too many attempts The atm ate your card.\n Good Bye")
#
# jason = Owner("Jason",1000,"Chase",1234567,"monkey")
# print(jason)
#
# jason.check_owner_info(1234567)
