import random
l = [random.randint(1,50) for i in range(10) ]

min = l[0]
index = 0
for i in range(0, len(l)-1):
    for j in range(i+1, len(l)):
        if l[i] > l[j]:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
print(l)