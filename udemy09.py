mystring='hamouda'
mylist=[]
for letter in mystring:
    mylist.append(letter)  #here we append the string to the list  by adding the letters
print(mylist)
print('hello hamoud')
mystring1='engineering'
mylist1=[letter for letter in mystring1]
print(mylist1)
mylist2=[x for x in 'syria inshallah will be better']
print(mylist2)
mylist3=[x for x in range(0,11)]
print(mylist3)
numlist=[num**2 for num in range(0,12)]  # it will print the square of each element
print(numlist)
evenlist=[n for n in range(0,14) if n%2==0]
print(evenlist)
evenlist=[n**2 for n in range(0,14) if n%2==0]
print(evenlist)  #the square of the even numbers numbers
celcius=[0,10,20,34.5,55.5]
fahrenheit=[((9/5)*temp+32) for temp in celcius]
print(fahrenheit)
result=[x if x%2==0 else 'odd' for x in range(0,12) ]  # if else inside the list
print(result)
list6=[]
for x in [2,3,4,5]:
    for y in [100,200,300]:
        list6.append(x*y)
print(list6)
mylist=[x*y for x in [2,3,5] for y in [100,200,300]]