def combination(n,k):
    product=1
    for i in range(n,k-1,-1):
        product=product*i
    for j in range(1,k+1):
        product=int(product/j)
    return product
inp=input('Enter n: ')
inp2=input('Enter k: ')
print(combination(inp,inp2))
