class student:
#initilize function .
     def __init__(self,name,major,gpa, probation):
         self.name=name  #the name of the object student = the name  that we passed in
         self.major=major #the major of the object student = the major we passed in
         self.gpa=gpa
         self.probation=probation
     def on_honor_roll(self):
         if self.gpa >=3.6:
             return True
         else:
             return False
     def  test(self):
         if self.major=="SE":
             return True
         else:
             return False