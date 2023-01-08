class Animal():
    def __init__(self,name):
        self.animal_name=name
    def speak(self):
        raise NotImplementedError("subclass not implement this abstract method")

class Dog(Animal):
    def speak(self):
        return self.animal_name+" says dog voice is woof"

class Cat(Animal):
    def speak(self):
        return self.animal_name+"cat voice meo"
bob=Dog("bob")
soso=Cat("soso")
print(bob.speak())
print(soso.speak())
