#using Dictionaries, store different types of data
month_conversion={
    "jan":"january" ,
    "mar":"march" ,
    "nov":"novmeber" ,
    "oct":"october" ,
    "Dec":"december",
    9 :"septmeper" ,
}
print(month_conversion)
print(month_conversion["nov"])
print(month_conversion.get("Dec"))
print(month_conversion.get("july","it's not a valid value"))
#while Loops
#excute cpde multiple times
i=1
while i<=10:
    print(month_conversion["nov"] , i)
    i+=1
print("done and i value is:",i)








