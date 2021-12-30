import numpy as np
with open('test.txt') as f:
    lines = f.readlines()
data=[]
for row in lines:
    print(row)
    data.append([int(x) for x in row.split(',')])
[data]=data
print(data)

for k in range(10):
    
    data[:] = [number - 1 for number in data]#[1,2,3,4]->[0,1,2,3]
    for n, i in enumerate(data):

        if i==-1:
            data[n]=6
            data.append(8)
            

    print("after day ",k+1 ,data,len(data))
#print(len(data),k)
##print(pow(2,7))