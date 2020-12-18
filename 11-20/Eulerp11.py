try:
    fhandle=open('EulerProblem11.txt')
except:
    print('File could not be found')
num_list=[]
complete_list=[]
for line in fhandle:
    line.strip()
    line.replace('\n','')
    num_list=line.split(' ')
    complete_list.append(num_list)
print(len(complete_list))
for i in range(0,20):
    for j in range(0,20):
        complete_list[i][j]=int(complete_list[i][j])
max_product=None

for i in range(0,20):
    for j in range(0,17):
        product=1
        for num in range(0,4):
            product=product*complete_list[i][j+num]
            if max_product==None or product>max_product:
                max_product=product
                horizontal=j
                vertical=i
print('Current max after linear is',max_product,'at position',vertical,horizontal)

for i in range(0,17):
    for j in range(0,20):
        product=1
        for num in range(0,4):
            product=product*complete_list[i+num][j]
            if max_product==None or product>max_product:
                max_product=product
                horizontal=j
                vertical=i
print('Current max after vertical is',max_product,'at position',vertical,horizontal)

for i in range(0,17):
    for j in range(0,17):
        product=1
        for num in range(0,4):
            product=product*complete_list[i+num][j+num]
            if product>max_product:
                max_product=max_product
                horizontal=j
                vertical=i
print('Current max after diagnol right is',max_product,'at position',vertical,horizontal)

for i in range(0,17):
    for j in range(0,17):
        product=1
        for num in range(0,4):
            product=product*complete_list[i+num][3+j-num]
            if product>max_product:
                max_product=product
                horizontal=3+j
                vertical=i
print('Max after diagnol left is',max_product,'at position',vertical,horizontal)
