def myfunc(item):
 result = ""
 for index, letter in enumerate(item):
     if index % 2 == 0:
         result += letter.upper()
     else:
         result += letter.lower()
 return result
print(myfunc('hamouda'))
