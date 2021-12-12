import numpy as np
with open('test.txt') as f:
    lines = f.readlines()
with open('advent5.txt') as t:
    line = t.readlines()
data =[]
data2=[]
data3=[]
for row in lines:
    data.append([x for x in row.split('->')]) # creates nested list of integers
for row in data:
    for clan in row:
        data2.append([i.strip() for i in row])
        break
for row in data2:
    for clan in row:
        #for c in clan:
        data3.append([int(x) for x in clan.split(',')])
print(data2)
#print(data2[0][1][0])
a = np.zeros(shape=(10,10))
#print(data3)
#a[4:1,5:2]=a[4:1,5:2]+1
#print(a)
for i in range(10):
    if data2[i][0][2]==data2[i][1][2]:#9 x1=x2
        y1=int(data2[i][0][2])
        y2=int(data2[i][1][2])
        x1=int(data2[i][0][0])
        x2=int(data2[i][1][0])
        a[y1,x1:x2+1]=a[y1,x1:x2+1]+1   
        a[y1,x2:x1+1]=a[y1,x2:x1+1]+1
    
    if data2[i][0][0]==data2[i][1][0]:#9 y1=y2
        y1=int(data2[i][0][2])
        y2=int(data2[i][1][2])
        x1=int(data2[i][0][0])
        x2=int(data2[i][1][0])
        a[y1:y2+1,x1]=a[y1:y2+1,x1]+1   
        a[y2:y1+1,x1]=a[y2:y1+1,x1]+1
print(a)
s=np.argwhere(a > 1)
print(len(s))
