from datetime import datetime
from datetime import   date
import math
import random
today=datetime.today()
print(datetime.today())
print(datetime.now())
new=today.replace(year=2020)
print(new)
date1=date(2023,11,3)
date2=date(2024,11,3)
print(date2-date1)
value=4.5
print(math.floor(value))
print(math.ceil(value))
print(round(value))
print(math.pi)
from math import  pi
print(pi)
print(math.e)
print(math.tau)
print(math.inf)
print(math.log(math.e))
print(math.log(10))
print(math.e**2)

# math.log(x,base)
print(math.log(100,10))
print(math.sin(10))
print(math.radians(180))
print(random.randint(10,100))
mylist=[2,3,4,5,5,4,3,3,3,2,2,2,1,4,44,55,66,2,4,455,32,56,32,12,32]

print(random.choices(population=mylist,k=10))
print(random.sample(population=mylist,k=10))
print(random.shuffle(mylist))
print(random.uniform(a=0,b=100))
print(random.gauss(mu=))




