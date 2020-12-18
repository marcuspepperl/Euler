grand_sum=0
for i in range(1,10001):
    num_to_i=0
    for j in range(1,int(i/2+1)):
        if i%j==0:
            num_to_i+=j
    if num_to_i>i:
        num_to_num_to_i=0
        for k in range(1,int(num_to_i/2+1)):
            if num_to_i%k==0:
                num_to_num_to_i+=k
        if i==num_to_num_to_i:
            print(i,' ',num_to_i)
            grand_sum=grand_sum+num_to_i+num_to_num_to_i
print('\n\nThe grand sum is', grand_sum)
