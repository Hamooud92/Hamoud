
my_file=open('hm.txt',"r")
print(my_file.readlines())
my_file=open('hm.txt',"r")
print(my_file.read())
my_file=open('hm.txt',"r")
print(my_file.seek(0))
new_file=open('C:\\Users\\Hamoud\\OneDrive\\Desktop\\HPE.txt')
print(new_file.read())
new_file.seek(0) #it's return back the cursor to the  beggining of the file
new_file.close()
with open('C:\\Users\\Hamoud\\OneDrive\\Desktop\\HPE.txt') as hamoud_file:
    content=hamoud_file.read()
print(content)
with open('C:\\Users\\Hamoud\\OneDrive\\Desktop\\HPE.txt') as hm_file:
     print(hm_file.read())


with open('C:\\Users\\Hamoud\\OneDrive\\Desktop\\new_hm.txt',mode='w') as new_new:
    new_new.write('hello hamoud ,welcome anytime')
with open('C:\\Users\\Hamoud\\OneDrive\\Desktop\\new_hm.txt') as new_new:
    print(new_new.read())
with open('hmy.txt',mode='w') as f:
    f.write('this to create a new file')
with open('hmy.txt',mode='r') as f:
    print(f.read())
my_str='hamouda'
print(len(my_str))
print(len(my_str)-1)
mid=my_str[1:-1]
print(mid)
result= my_str[-1]+mid+my_str[0]
print(result)
result2=my_str[len(my_str)-1] +my_str[1:len(my_str)-1]+my_str[0]  # my_str[1:len(my_str)-1]
print(result2)

