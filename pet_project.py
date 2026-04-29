class Pet():
    def _init_(self, name, happy, fetch, happiness):
        self.name = name
        self.__happy = happy
        self.fetch = fetch
        self.happiness = happiness
    

class Interact():

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

    def interact(self, fetch):
        self.happiness.append(fetch)
        print(self.happiness)

Dog = Pet("Dog", 100, "fetch", 50)
Dog.interact(50)

print(Dog.__dict__)