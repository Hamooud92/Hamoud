def count_prime(num):
    if num <2:
        return 0
    primes=[2]
    x=3
    #x is going through each number  up to the input number "num"
    while x<=num:
        #check if x is prime
        for y in primes:
            if x%y==0 :
                x+=2
                break
            else:
                primes.append(x)
                x+=2
    print(primes)
    return  len(primes)
count_prime(100)


