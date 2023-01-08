work_month=[('hamoud',2000),('sami',350),('omar',3003)]
print(work_month)
def optimal(work_month):
    a_employee=''
    max_hours=0
    for employee,hours in work_month:
        if hours>max_hours:
            max_hours=hours
            a_employee=employee
        else:
            pass
    return  (a_employee,max_hours)
print(optimal(work_month))
# interactions between  functions
# mimic the carnival guessing game"Three cup monte"
 