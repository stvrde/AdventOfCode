with open('advent2.txt') as f:
    lines = f.readlines()

def prvi_dio():
    suma=0
    suma2=0
    suma3=0
    for l in lines:
        if "forward" in l:
        
            res = [int(i) for i in l.split() if i.isdigit()]
            
            for i in res:
                suma= suma +i
        if "up" in l:
            res = [int(i) for i in l.split() if i.isdigit()]
            for i in res:
                suma2=suma2 +i
        if "down" in l:
            res = [int(i) for i in l.split() if i.isdigit()]
            for i in res:
                suma3=suma3 +i
    print(suma*(suma3-suma2))

#--------drugi dio----------

def drugi_dio():
    
    forward=0
    aim=0
    depth=0
    s=0

    for l in lines:

        if "forward" in l:
        
            s=int(l.strip("forward "))
            depth = (s * aim) + depth
            forward = forward + s
            

        if "up" in l:
            
            s=int(l.strip("up "))
            aim = aim - s
            
        if "down" in l:
            
            s=int(l.strip("down "))
            aim = aim + s
    return forward*depth
    #print("forward", forward, "depth", depth, "aim" ,aim)
print(drugi_dio())