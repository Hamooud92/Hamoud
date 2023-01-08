def spy(nums):
    code=[0,0,7,'x']
    for num in nums :
        if num==code[0]:
            code.pop(0) # each time pop element from the list until it contains just 'x'
    return len(code)==1
print(spy([0,0,1,2,4,7,3]))

def count_primes(num):
    primes=[2]
    x=3  #start  examine the numbers start of 3
    if num<2 :  #to test 1 and 2 case 1 and 2 by convention is primary
        return 0
    while num>=x:  # bigger than 3
        for y in range(3,x,2):
            if x%y==0:   # not primary
                x+=2
                break
        else:
            primes.append(x)  # add to the primary list
            x+=2
    print(primes)
    return  len(primes)
print(count_primes(35))