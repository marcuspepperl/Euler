try:
    fhandle=open('100largenumbers.txt')
except:
    print('Opening error')
total=0
for line in fhandle:
    line.strip()
    line.replace('\n','')
    line=int(line)
    total=total+line
total=str(total)
count=0
for i in range(10):
    print(total[i])
