import math
product=1
for i in range(1,101):
    product=product*i
product_string=str(product)
sum=0
for ch in product_string:
    ch=int(ch)
    sum+=ch
print(sum)
