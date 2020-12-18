max_list=1
pos=None
for i in range(2,1000000):
    store=i
    count=1
    while(i>1):
        if i%2==0:
            i=int(i/2)
        else:
            i=3*i+1
        count+=1
    if count>max_list:
        max_list=count
        pos=store
print(pos,'has a length of',max_list)
