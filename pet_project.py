class Pet():
    def _init_(self, name, age, happy):
        self.name = name
        self.age = age
        self.__happy = happy

    def interact(self):
        return f"{self.name} is playing fetch"
    
"""     def happy_level(self, joy):
        self.__happy += joy

    def show_happy_level(self):
        print(f"{self.name}'s happiness is now {self.__happy}")

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory) """


my_pet = Pet("Dog", "2", "50")
print(my_pet.interact())

""" class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # double underscore means "private"

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(f"{self.owner} has ${self.__balance}")
Jillian =BankAccount("Jillian",2)
Jillian.deposit(50)
print(Jillian.__dict__) """