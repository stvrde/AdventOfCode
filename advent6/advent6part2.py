import numpy as np
import collections

with open('advent6.txt') as f:
    lines = f.readlines()
data=[]
for row in lines:

    data.append([int(x) for x in row.split(',')])
[data]=data

prvi,drugi,treci,cetvrti,peti = 0,0,0,0,0 #dont look my cat wrote this part of code
for i in data:
    if i ==1:
        prvi=prvi+1
    if i== 2:
        drugi = drugi+1
    if i == 3:
        treci = treci+1
    if i == 4:
        cetvrti = cetvrti+1
    if i == 5:
        peti = peti+1
radna=[0,prvi,drugi,treci,cetvrti,peti,0,0,0]    


d = collections.deque(radna) #make deque so i can rotate to the left 


for k in range(256):
    d.rotate(-1)
    d[6]=d[8]+d[6]


print("Number of 0-8 day fish in order: ",d)
print("Solution: ",sum(d))
