import re
text="this is Hamoud ,how  are you  408-555-1234"
a='hamoud' in text
print(a)
A='Hamoud' in text
print(A)
pattern='how'
print(re.search(pattern,text))
c=re.search(pattern,text)
print(c)
print(c.span())
print(c.end())
print(c.start())
match=re.findall('is',text)
print(match)
print(len(match))
for xx in re.finditer('is',text):
    print(xx.span())
    print(xx.group())
data="this is Hamoud ,how  are you  408-555-1234"
phone1=re.search('408-555-1234',data)  #search for exact number
print(phone1)
phone2=re.search(r'\d\d\d-\d\d\d-\d\d\d\d',data) #pattern /regular expression  ,search for changable numbers.
phone3=re.search(r'\d{3}-\d{3}-\d{4}',data)
print(phone2)
print(phone3)
print(phone1.group())
print(phone2.group())
phone_pattern=re.compile(r'(\d{3})-(\d{3})-(\d{4})')
result=re.search(phone_pattern,data)
print(result)
print(result.group())
print(result.group(1))
print(result.group(2))
print(result.group(3))
print(re.search(r'cat','the cat is here'))
print(re.search(r'dog|cat','the dog is here'))
print(re.findall(r'.at','there is at least 1 cat at th box'))
print(re.findall(r'...at','there is at least three cats at tbe bat splat'))
print(re.findall(r'^\d','3 is a number')) # just to search in a text that start  with a number
print(re.findall(r'\d$','3 is a number 5')) # just to search in a text that end  with a number
phrase='there is 5 numbers ! 34 inside  5 ! this sentence!! .. ?'
nums=r'[^\d]+'  # it will exclude all the numbers
print(re.findall(nums,phrase ))
chars=r'[^!.?]+'
clean =re.findall(chars,phrase)
print(clean)
join_clean=''.join(clean)
print(join_clean)
data2='find only the hypen-word in this sentence word-word ,hm in Turkey now and love Allah'
patteren2=r'[\w]+-[\w]+'
print(re.findall(patteren2,data2))
t1='hello catfish'
t2='hello catnap'
print(re.search(r'cat(fish|nap)',t1))
print(re.search(r'cat(fish|nap)',t2))