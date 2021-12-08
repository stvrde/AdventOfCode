import numpy as np
from io import StringIO
with open('valjda.txt') as f:
    lines = f.readlines()
with open('advent4numbers.txt') as t:
    line = t.readlines()

def new():


    numbers=[22,8,21,6,1,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
    #print(b)
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
    print(b)

    for number in numbers:
        row_sums=0
        broj_retka=0
        row_columns=0
        
        for row in b:
            row_sums = b[broj_retka-1].sum() #checks for horizontal bingos
            
            #print(row_sums,"suma retka", broj_retka, "redak",s,"broj")
            #print(row_columns)
            if row_sums != -5 and row_columns != -5: #if no vertical or horizontal bingos do
                broj_stupca=-1
                broj_retka=broj_retka+1
                
                #print(broj_retka,"broj retka ")   
                for member in row:                
                    
                    broj_stupca=broj_stupca+1   
                    manji_broj=(broj_retka // 5) * 5
                    veci_broj=((broj_retka // 5)+1) * 5
                    row_columns=b[manji_broj:veci_broj, broj_stupca].sum() # checks for vertical bingos
                    #print(number,"numberlol")
                   
                    if row_columns==-5:
                        #print(number,"number ispis")
                        #return broj_retka,b,manji_broj,veci_broj,7#daje jedan broj vise, stupci ne
                        b = np.where(b<0,0,b)
                        leftover_sum=b[manji_broj:veci_broj].sum()
                        print(b,leftover_sum,leftover_sum*number,"rowcolumns",number)
                        break
                    if number==member:
                        b[broj_retka-1,broj_stupca]=-1          
                        #print(manji_broj,"manji broj", veci_broj, "veci broj")
                        #print(row_columns,"row columns")          
                    
            else:
                b = np.where(b<0,0,b)
                leftover_sum=b[manji_broj:veci_broj].sum() # vraca array di je naden bingo i vraca redak u kojen se desilo. triba napravit za stupce jos
                print(b,leftover_sum*number,"donji else",number,leftover_sum)
                break

def sum_rest(broj_retka,b,manji_broj,veci_broj,number):
    print(broj_retka,b,number,"number",manji_broj)
    b = np.where(b<0,0,b)#replaces all elements < 0 with 0 in array
    print(b,"bbbbbbbb")
    leftover_sum=b[manji_broj:veci_broj].sum()
    print(leftover_sum,leftover_sum*number)

#broj_retka,b,manji_broj,veci_broj,number=new()
#sum_rest(broj_retka,b,manji_broj,veci_broj,12)
print(new())