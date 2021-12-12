import numpy as np
with open('advent5.txt') as f:
    lines = f.readlines()
data =[]
data2=[]

for row in lines:
    data.append([x for x in row.split('->')]) #
for row in data:
    for clan in row:
        data2.append([i.strip() for i in row])
        break

data3=[]
for row in data2:
    for clan in row:
        data3.append(tuple([int(x) for x in clan.split(',')]))

data2 = [data3[x:x+2] for x in range(0, len(data3), 2)]#from 4-19 manipulating input data to get nested list of tuples

a = np.zeros(shape=(1000,1000))#10000x10000 array with zeros

for i in range(len(data2)):
    y1=int(data2[i][0][1])
    y2=int(data2[i][1][1])
    x1=int(data2[i][0][0])
    x2=int(data2[i][1][0])
    if data2[i][0][1]==data2[i][1][1]:# x1=x2 horizontal lines

        a[y1,x1:x2+1]=a[y1,x1:x2+1]+1   
        a[y1,x2:x1+1]=a[y1,x2:x1+1]+1

    if data2[i][0][0]==data2[i][1][0]:# y1=y2 vertical lines

        a[y1:y2+1,x1]=a[y1:y2+1,x1]+1   
        a[y2:y1+1,x1]=a[y2:y1+1,x1]+1

    if abs(x1-x2) == abs(y1-y2):#diagonals


        if x1<x2 and y1<y2: #(0,0)->(8,8)
            for i, j in zip(range(x1,x2+1), range(y1,y2+1)):

                a[j,i]=a[j,i]+1   
        if x1>x2 and y1>y2:
            for i, j in zip(range(x2,x1+1), range(y2,y1+1)):#(6,4)->(2,0)

                a[j,i]=a[j,i]+1
        if x1>x2 and y1<y2:
            for i, j in zip(reversed(range(x2,x1+1)), range(y1,y2+1)):#(8,0)->(0,8)

                a[j,i]=a[j,i]+1
            
        if x1<x2 and y1>y2:
            for i, j in zip(range(x1,x2+1), reversed(range(y2,y1+1))):#(5,5)->(8,2)

                a[j,i]=a[j,i]+1
    

s=np.argwhere(a > 1)
print("Number of overlaps > 1: ",len(s))

