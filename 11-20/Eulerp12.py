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
def triangular_min_divisors(numb):
    val=2
    while(True):
        if val%2==0:
            a=int(val/2)
            b=val+1
        else:
            a=val
            b=int((val+1)/2)
        dict1=prime_strip(a)
        dict2=prime_strip(b)
        for entry in dict2:
            dict1[entry]=dict1.get(entry,0)+dict2[entry]
        divisors=1
        for entry in dict1:
            divisors=divisors*(dict1[entry]+1)
        if divisors>numb:
            print(val,int(val*(val+1)/2))
            break
        val+=1
triangular_min_divisors(500)
