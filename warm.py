def string_times(str, n):
  result=""
  for i in range(n):
    result=result+str
  return result
print(string_times('hm',5))
s='hello'
print(s[1])
list4=[4,33,2,44,3]
print(list4)
#print(list4.sort())
print(list4)
d={'sk':'www'}
print(d.values())
print(d['sk'])
d1={'k1':{'k2':'hello'}}
print(d1['k1']['k2'])
ddd={'k1':[{'nest_key':['this is deep',['hello']]}]}
print(ddd['k1'][0]['nest_key'][1])
print(s[::-1]) #it will revers the string
sorted(list4)
def evs(str):
  rrr=""
  for p in range(len(str)):
    if p%2==0:
      rrr=rrr+str[p]
  return rrr
evs('hmhmy')
print(evs('hamouda'))
2*str[0]+str[1]+str[0::]