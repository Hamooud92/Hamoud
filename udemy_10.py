def say_hi(name):
    print(f'hello {name}')
say_hi('Hamoud')
def add_num(num1,num2):
     return num1+num2
result=add_num(2,4)
print(result)
def return_result(a,b):
    return a+b
c=return_result(3,5)
print(c)
# pay attention when you receive data from the user ,sum numbers  or stringss or char
def front_times(str,n):
    front_len=3
    if front_len>len(str):
        front_len=len(str)
    front=str[:front_len]
    result=""
    for i in range(n):
        result=result+front
    return result
nnn=front_times('hm',3)
print(nnn)



def string_splosion(str):
  result1=""
  for i in range(len(str)):
    result1=result1+ str[:i+1]
  return result1
bb=string_splosion('code')
print(bb)


def last2(str):
    if len(str)<2:
        return 0
    count=0
    last2=str[len(str)-2:]
    for i in range(len(str)):
        sub=str[i:i+2]
        if sub==last2:
            count=count+1
    return count
ccc=last2('hmyhmy')
print(ccc)

def array_count9(nums):
 count=0
 for i in range(len(nums)):
   if nums[i]==9:
     count=count+1
 return count
aa=array_count9([1,9,9,9,2,3,55,9])
print(aa)

def string_match(a, b):
  shorter=min(len(a),len(b))
  count=0
  for i in range(shorter-1):
    a_sub=a[i:i+2]
    b_sub=b[i:i+2]
    if a_sub==b_sub:
      count=count+1
  return count
bb=string_match('hamoudhmhm','hamoudhmhmy')
print(bb)

def string_times(str, n):
  result = ""   # n*str
  for i in range(n):  # range(n) is [0, 1, 2, .... n-1]
    result = result + str  # could use += here
  return result
dd=string_times('hm',3)
print(dd)

