class Animal():
    def __init__(self):
        print("Animal created")
    def who_ami(self):
        print("i  am an animal")
    def eat(self):
        print("i am eating ,ok cheers")
myanimal=Animal()
print(myanimal.who_ami())
#print(myanimal.eat())


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
    def who_ami(self):
        print("i'm a dog ")
    def bark(self):
        print("i am barking .WOOF!")
    '''def eat(self):
        print("hello ,eat this is override")'''

my_dog=Dog()

my_dog.eat()
my_dog.who_ami()
my_dog.bark()
#polymorphisim: many object classess  shared the same methods

class Car():
    def __init__(self,name):
        self.car_name=name
        print("this is a car ")
    def has_wheels(self):
        return  self.car_name+" is hamoud car and has wheels"
hamoud_car=Car('sss')
print(hamoud_car.has_wheels())


class Bus():
    def __init__(self,name):
        self.bus_name=name
        print("this is a bus ")
    def has_wheels(self):
        return  self.bus_name+" is hamoud bus and has wheels"
toyota=Car("toyota")
kadmous=Bus("kadmous")
print(toyota.has_wheels())
print(kadmous.has_wheels())
for transport in [toyota,kadmous]:
    print(type(transport))
    print(type(transport.has_wheels()))

def transport_has_wheels(transport):
    print(transport.has_wheels)
print(transport_has_wheels(toyota))
transport_has_wheels(kadmous)





