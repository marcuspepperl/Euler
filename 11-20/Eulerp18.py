try:
  fhandle=open('Maximum Path Sum 1.txt')
except:
  print('Error in opening file\n')
  quit()
num_list=[]
complete_list=[]
for line in fhandle:
     line.strip()
     line.replace('\n','')
     num_list=line.split(' ')
     complete_list.append(num_list)
for i in range(0,15):
    for j in range(0,i+1):
        complete_list[i][j]=int(complete_list[i][j])
print(complete_list)
for i in range(14,0,-1):
    for j in range(0,i):
        if complete_list[i][j]>complete_list[i][j+1]:
            pair_max=complete_list[i][j]
        else:
            pair_max=complete_list[i][j+1]
        complete_list[i-1][j]=pair_max+complete_list[i-1][j]
print(complete_list[0][0])
