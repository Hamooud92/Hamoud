def raise_to_power(base_num,pow_num):
    result =1
    for index in range(pow_num):
        result*=base_num
    return  result
print(raise_to_power(3,2))

'''
comments 

'''
state_capitals = {
 'Arkansas': 'Little Rock',
 'Colorado': 'Denver',
 'California': 'Sacramento',
 'Georgia': 'Atlanta'
}
ca_capital = state_capitals['California']
for k in state_capitals.keys():
 print('{} is the capital of {}'.format(state_capitals[k], k))



 print(dir(__builtins__))
 help(max)
