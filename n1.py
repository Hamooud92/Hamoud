from student import student
#create object ,it's an instance of the class
student1=student("Hamoud","IT enginner",3.8,False)
student2=student("Sami","SE",3.8,True)
print("student name is: " +student1.name+ " and his major is: "+student1.major)
print(student1.probation)

print(student2.on_honor_roll())
print(student1.on_honor_roll())
print(student1.test())
print(student2.test())

