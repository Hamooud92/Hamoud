mylist=[1,2,3]
myset=set()
print(type(myset))

class Sample():
    pass
my_sample=Sample()
print(type(my_sample))

class Dog():
    species='moon'   #class object attributes

    def __init__(self,breed,name,spots):
        self.attributes_breed=breed
        self.attributes_name=name
        self.attributes_spots=spots
    #note:the methode is  a function that written insode the class
    def bark(self,number):
        print("my name is {} and the number is: ".format(self.attributes_name,number))

my_dog=Dog(breed='lab',name='bob',spots='black')   #create instance
print(type(my_dog))
print(my_dog.attributes_breed,my_dog.attributes_name,my_dog.attributes_spots)

print('the spots of the dog is   : '+my_dog.attributes_spots)
print(my_dog.species)
print(my_dog.bark(5))


class Circle():
    pi=3.14
    def __init__(self,radius=1):
        self.c_radius=radius
        self.area=radius*radius*self.pi
    def get_circumference(self):
        return self.c_radius*2*self.pi
my_circle=Circle()
jarrah_circle=Circle(3)
print(my_circle.get_circumference())
print(jarrah_circle.get_circumference())
print(my_circle.area)
print(jarrah_circle.area)

