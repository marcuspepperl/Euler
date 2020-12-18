import math
def prime_sum(n):
    sum=2
    for i in range(3,n,2):
        max_check=int(math.sqrt(i))
        prime=True
        for j in range(3,max_check+1,2):
            if int(i%j)==0:
                prime=False
                break
        if prime==True:
            sum=sum+i

    return sum
print(prime_sum(2000000))
