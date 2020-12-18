num=600851475143
greatest_factor=None
while(num>1):
    for i in range(3,10000,2):
        if num%i==0:
            num=num/i
            if greatest_factor==None or i>greatest_factor:
                greatest_factor=i
            break
print('The greatest prime factor is ',greatest_factor)
