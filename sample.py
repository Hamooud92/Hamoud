class Simple():

    def __init__(self,value):
        self.value=value
    def add_to_value(self,amount):
         self.value=self.value+amount
mysimple=Simple(300)
print(mysimple.value)
print(mysimple.add_to_value(500))
print(mysimple.value)
if__name__=="__main__":
