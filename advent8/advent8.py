with open('advent8.txt') as f:
    lines = f.readlines()
data=[]
for row in lines:

    data.append([x.strip('\n') for x in row.split(' ')])

nova=[]
for i in data:

    for s in i[-4:]:

        nova.append(len(s))

counter= 0
for number in nova:
    if number == 2 or number == 3 or number == 4 or number == 7:
        counter +=1
print("Solution part 1: ",counter)