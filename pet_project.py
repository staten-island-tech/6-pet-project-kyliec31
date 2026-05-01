class Pet():
    def __init__(self, name, happy):
        self.name = name
        self.__happy = happy

    def interact(self):
        return f"{self.name} is playing fetch"

    def happy_level(self, amount):
        self.__happy += amount

    def show_happy_level(self):
        print(f"{self.name}'s happiness is now {self.__happy}")


my_pet = Pet("Dog", 0)
play = input("Do you want to play with your pet? : ")
while play == "yes":
    my_pet.happy_level(20)
    print(my_pet.__dict__)
    print("Your pet's happy level increased by 20!")
    
    continue_playing = input("Would you like to continue playing with your pet? : ")
    if continue_playing == "yes":
            my_pet.happy_level(20)
            print(my_pet.__dict__)
            print("Your pet's happy level increased by 20!")
    else:
            break


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