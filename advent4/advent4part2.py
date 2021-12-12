import numpy as np


with open('advent4.txt') as f:
    lines = f.readlines()
data =[]
for row in lines:
    data.append([int(x) for x in row.split()]) # creates nested list of integers
del data[6-1::6]

numbers=[17,11,37,7,89,48,99,28,56,55,57,27,83,59,53,72,6,87,33,82,13,23,35,40,71,47,78,2,39,4,51,1,67,31,79,69,15,73,80,22,92,95,91,43,26,97,36,34,12,96,86,52,66,94,61,76,64,77,85,98,42,68,84,63,60,30,65,19,54,58,24,20,25,75,93,16,18,44,14,88,45,10,9,3,70,74,81,90,46,38,21,49,29,50,0,5,8,32,62,41]
lista2=[]

for s in data:
    for d in s:
        lista2.append(int(d))

a =np.array(lista2)
moje=np.array(lista2)
duljina=len(lista2)//5
b=np.reshape(a,(duljina,5)) #making array to work with
moje2=np.reshape(moje,(duljina,5))#array to get last number later

popis=[]
popis2=[]
sume=[]
for number in numbers:
    s=np.argwhere(b==number) #finds all positions in array where lottery number == number on board

    for i in s:

        b[i[0],i[1]]=-1 #set all number that are out to -1
        row_sums = b[i[0]].sum() 
        manji_broj=(((i[0]) // 5) * 5)
        veci_broj=manji_broj+5
        column_sums=b[manji_broj:veci_broj,i[1]].sum()

        if row_sums==-5 or column_sums==-5:
            popis.append((i[0],i[1])) # makes list of all positions when bingos are pulled out
            popis2.append(veci_broj//5) # another list of boards when bingos are pulled out
            nule = np.where(b<0,0,b) # return all numbers set on -1 to 0 so we can get sum of boards
            leftover_sum=nule[manji_broj:veci_broj].sum() #gets leftover sum on boards

            sume.append(leftover_sum) #makes list of sums after each bingo


res = []
[res.append(x) for x in popis2 if x not in res] #remove duplicates from popis2, last memeber of this list is last board that is pulled out

brojac=0
for i in popis2: #gets position of last pulled number 
    brojac=brojac+1
    if i == res[-1]:
        break

print("Suma zadnjeg: ",sume[brojac-1])
f=popis[brojac-1]
print("Zadnji broj: ",moje2[f[0],f[1]])
print("Rezultat :", sume[brojac-1]*(moje2[f[0],f[1]]))
