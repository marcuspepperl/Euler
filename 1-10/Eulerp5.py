import math
def prime_strip(n):
    store=n
    prime_dict={}

    while(n>1):
        if int(n%2)==0:
            n=int(n/2)
            prime_dict[2]=prime_dict.get(2,0)+1
        else:
            last=3
            for num in range(last,int(n+1),2):
                if int(n%num)==0:
                    n=int(n/num)
                    prime_dict[num]=prime_dict.get(num,0)+1
                    last=num
                    break
    return prime_dict


def lcm(val):
    greatest_prime_dict={}

    for i in range(2,val+1,1):
        dict_returned=prime_strip(i)
        for factor in dict_returned:
            if dict_returned[factor]>greatest_prime_dict.get(factor,0):
                greatest_prime_dict[factor]=dict_returned[factor]

    lcm=1
    for prime in greatest_prime_dict:
        lcm=lcm*(prime**greatest_prime_dict[prime])

    print(greatest_prime_dict)
    if math.log10(lcm)>30:
        length=int(math.log10(lcm))
        lcm_str=str(round(lcm/(10**(length)),10))+'*10^'+str(length)
        print('\nThe least common multiple of the first',val,'numbers is\n',lcm_str)
    else:
        print('The least common multiple of the first',val,'numbers is\n',lcm)
    return lcm

inp=input('Enter a value: ')
try:
    inp=int(inp)
except:
    print(inp,'is not a number')
    quit()
lcm(inp)
