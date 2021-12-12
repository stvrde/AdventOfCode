

with open('advent.txt') as f:
    lines = f.readlines()

def advent(novalista):
    lista=[]
    lista1=[]
    substract=[]
    for num in novalista:
        lista.append(num)
        lista1.append(num)
    lista1.pop(0)
    lista.pop()
    for (item1, item2) in zip(lista, lista1):
        substract.append(int(item2)-int(item1))

    solution = 0
    for i in substract:
        if int(i) > 0:
            solution += 1
    print("Solution",solution)

def advent2():

    lista=[]
    lista2=[]
   
    #makes list out of .txt file
    for num in lines:
        lista.append(num)

    # makes triplets
    br = 0
    for i in lista[:-2]:
        
        lista2.append(lista[br:br+3])
        br+=1

    #converts to integer and returns list of triplets sums
    test_list=[]
    novalista=[]
    for i in lista2:
        test_list = list(map(int, i))
        novalista.append(sum(test_list))
      
    return novalista

advent2()
advent(advent2())

