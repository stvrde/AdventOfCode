
with open('advent7.txt') as f:
    lines = f.readlines()

def factor(n): #for second part to get sum1-4 = 6 , 1-5=10 etc
    suma=0
    for br in range(0,n+1):
        suma+=br
    return suma



data=[]
for row in lines:

    data.append([int(x) for x in row.split(',')])
[data]=data


novi=[]
print(len(data))
print(max(data),min(data)) #min number max number in data
for i in range(min(data),max(data)): #reduce all numbers by min to max and make list
    suma=0
    for d in data:
        novi.append(factor(abs(d-i)))  
sume=[]
chunks = [novi[x:x+len(data)] for x in range(0, len(novi), len(data))] # make small lists to length of first list

for g in chunks:    #sum of each chunk
    sume.append(sum(g))
print("Rjesenje: ",min(sume))


