
with open('advent7.txt') as f:
    lines = f.readlines()

data=[]
for row in lines:

    data.append([int(x) for x in row.split(',')])
[data]=data
#print(data)


novi=[]

for i in range(min(data),max(data)): #reduce all numbers by min to max and make list
    suma=0
    for d in data:
        novi.append(abs(d-i))  
sume=[]
chunks = [novi[x:x+len(data)] for x in range(0, len(novi), len(data))] # make small lists to length of first list


for g in chunks:    #sum of each chunk
    sume.append(sum(g))

print("Rjesenje: ",min(sume))


def factor(n):
    for i in range(n):
        i=i+1
    return i