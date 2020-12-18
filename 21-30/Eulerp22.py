def number_value(char):
    dict={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,
    'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    return dict.get(char,0)

fhandle=open('Eulerp22_names.txt')
entire_string=''
for line in fhandle:
    line.replace('\n','')
    entire_string=entire_string+line
names_list=entire_string.split(',')
names_list.sort()
total=0
for i in range(len(names_list)):
    score=0
    score_value=0
    position=i+1
    for ch in names_list[i]:
        score+=number_value(ch)
    score_value=position*score
    total+=score_value
print(total)
