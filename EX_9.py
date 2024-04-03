l1=[2, 3, 5, 8, 12]
l2=[9, 11, 14, 16, 19]

for i in l1:
    if (i%2!=0):
        print(i)

      
for j in l2:
    if (j%2==0):
        print(j)


print([i for i in l1 if (i%2!=0)]+[j for j in l2 if (j%2==0)])

#Exercise number 9
