import numpy as np

def make_matrix(): #vraca matricu , broj redaka i broj stupaca
    with open('test.txt') as f:
        lines = f.readlines()
    lista=[]
    print(lines)
    for l in lines:
        lista.append(l.strip())
        n=len(l)
    print(lista)
    lista2=[]
    for s in lista:
        for d in s:
            lista2.append(int(d))

    a =np.array(lista2)
    print(a,"aaaaaaa")
    s=int(len(a)/n)

    b=np.reshape(a,(s,n))
    #b matrica
    #s broj redaka
    #n broj stupaca

    return b,s,n

def find_commons(b,s,n): #nade gamma i epsilon i pomnozi ih
    
    gamma=[]
    epsilon=[]
    for i in range(0,n):
        

        column_sums = b[:, i].sum()
        if column_sums > s/2:
            c=1
            e=0
            gamma.append(c)
            epsilon.append(e)
        else:
            c=0
            e=1
            gamma.append(c)
            epsilon.append(e)   
    

    listToStrGamma = ''.join([str(elem) for elem in gamma])
    listToStrEpsilon = ''.join([str(elem) for elem in epsilon])
    #print(listToStrGamma,listToStrEpsilon)

    #print(int(listToStrGamma,2))
    #print(int(listToStrEpsilon,2))
   # print(int(listToStrGamma,2)*int(listToStrEpsilon,2))
        #print(column_sums,gamma,epsilon)


def oxygen(b,s,n): 
    
    i=0    
    counter=0
 
    for i in range(0,n):
        
        num_rows = np.shape(b)[0] 
        if num_rows >1:
            column_sums = b[:, i].sum()
            counter=0
            if column_sums >= s/2: #if column sum > rows/2 it means there is more ones than zeros
                c=1
                for br in b:
                    if br[i]== c:    

                        counter=counter+1

                    else:
                        b=np.delete(b,counter,0)

            elif  column_sums < s/2:  
                c=0
                for br in b:
                    if br[i]== c:
                        
                        counter=counter+1

                    else:
                        b=np.delete(b,counter,0)

            s=counter
            #print(b)
        else:
            return b


def dioksid(b,s,n): 
    
    i=0    
    counter=0
 
    for i in range(0,n):
        num_rows = np.shape(b)[0] 
        if num_rows >1:
            column_sums = b[:, i].sum()
            counter=0
            if column_sums < s/2:
                c=1
                for br in b:
                    if br[i]== c:    

                        counter=counter+1

                    else:
                        b=np.delete(b,counter,0)

            elif  column_sums >= s/2:  
                c=0
                for br in b:
                    if br[i]== c:
                        
                        counter=counter+1

                    else:
                        b=np.delete(b,counter,0)
            #print(b)
            s=counter
            #print(b)
        else:
            return b
"""
values=make_matrix()
a=oxygen(values[0],values[1],values[2])
g=dioksid(values[0],values[1],values[2])
listToStrGamma = ''.join([str(elem) for elem in a[0]])
listToStrEpsilon = ''.join([str(elem) for elem in g[0]]) #napravi string od prvog elemetna od arraya
print(int(listToStrGamma,2)*int(listToStrEpsilon,2)) #convertira binarni u decimalni i pomnozi
print(int(listToStrEpsilon,2))
"""
make_matrix()