import numpy as np
from numpy.lib.npyio import savetxt
with open('advent4.txt') as f:
    lines = f.readlines()

def new():

    numbers=[17,11,37,7,89,48,99,28,56,55,57,27,83,59,53,72,6,87,33,82,13,23,35,40,71,47,78,2,39,4,51,1,67,31,79,69,15,73,80,22,92,95,91,43,26,97,36,34,12,96,86,52,66,94,61,76,64,77,85,98,42,68,84,63,60,30,65,19,54,58,24,20,25,75,93,16,18,44,14,88,45,10,9,3,70,74,81,90,46,38,21,49,29,50,0,5,8,32,62,41]
    data =[]
    for row in lines:
        data.append([int(x) for x in row.split()]) # creates nested list of integers
    del data[6-1::6]

    lista2=[]
    for s in data:
        for d in s:
            lista2.append(int(d))

    a =np.array(lista2)
    duljina=len(lista2)//5
    b=np.reshape(a,(duljina,5)) #array s kojin radimo


    for number in numbers:
        row_sums=0
        broj_retka=0
        row_columns=0

        for row in b:
            row_sums = b[broj_retka-1].sum() #checks for horizontal bingos
            
            if row_sums != -5 and row_columns != -5: #if no vertical or horizontal bingos do
                broj_stupca=-1
                broj_retka=broj_retka+1

                for member in row:                
                    
                    broj_stupca=broj_stupca+1   
                    if broj_retka==0:
                        manji_broj=0
                        veci_broj=5
                    else:
                        manji_broj=(((broj_retka-1) // 5) * 5)
                        veci_broj=manji_broj+5
                    row_columns=b[manji_broj:veci_broj, broj_stupca].sum() # checks for vertical bingos

                   
                    if row_columns==-5:

                        return b,manji_broj,veci_broj,number,broj_retka#daje jedan broj vise, stupci ne
                 
                        

                    if number==member:
                        b[broj_retka-1,broj_stupca]=-1               
                    
            else:

                return b,manji_broj,veci_broj,number,broj_retka
      
def sum_rest(b,manji_broj,veci_broj,number,broj_retka):
    

    b = np.where(b<0,0,b)#replaces all elements < 0 with 0 in array
    leftover_sum=b[manji_broj:veci_broj].sum()
    print("last number", number)
    print("leftover sum",leftover_sum)
    print("leftover_sum*number",leftover_sum*number)

b,manji_broj,veci_broj,number,broj_retka=new()
sum_rest(b,manji_broj,veci_broj,number,broj_retka)

new()