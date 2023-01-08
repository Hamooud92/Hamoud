def my_s(str):
    result=""
    for i in range(len(str)):
        result=result+str[:i+1]
    return result
print(my_s('abc'))


#new
def dd(str):
 if len(str)<2:
      return 0
 last2=str[len(str)-2:]
 count=0
 for i in range(len(str)-2):
     sub=str[i:i+2]
     if sub==last2:
         count=count+1
 return count
print(dd('hmyhmy'))
my_str='hamouda'
for i in range(len(my_str)):
    print(my_str[i:i+2])
list5=[1,3,45,9]
print(len(list5))
a='hmyhmy'
b='hmshmyy'
def match_S(a,b):
    shorter=min(len(a),len(b))
    count=0
    for i in range(shorter-1):
        a_sub=a[i:i+2]
        b_sub=b[i:i+2]
        if a_sub==b_sub:
            count=count+1
    return count
print(match_S('hmyhmn','hmyhmz'))

test='hamoud'
print(len(test))
last2=len(test)-2
last3=test[len(test)-2:]

print(last2)
print(last3)
for i in range(len(test)-2):
    print(test[i:i+2])



def  second(str):
    if len(str)<2:
        return 0
    ff2=str[len(str)-2:]  # last two chars  of the string
    count=0
    for i in range(len(str)-2):
        sub=str[i:i+2]  #the sequence of the two
        if sub==ff2:
            count=count+1
    return count
print(second('myhmhmy'))

st='print only the words that star with s in this sentence'
for lll in st.split():
    print(lll)
    if lll[0].lower()=='s': #if lll[0]=='s or lll[0]=='S'
     print(lll)

for nn in range(0,11):
    if nn%2==0:
        print(nn)
print(list(range(0,11,2)))  #(start , end,step)
for iii in range(1,50):
    if iii%3==0:
        print(iii)
ccc=[x for x in range(1,51) if x%3==0]
print(ccc)
kk='print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word)%2==0:
        print(word+'this is even')
for num in range(1,101):
  if mum %3==0 and num %5==0:
      print('FizzBuzz')
  elif num%3==0:
      print('Fizz')
  else:
      print
for ch in kk.split():
   print(ch)
