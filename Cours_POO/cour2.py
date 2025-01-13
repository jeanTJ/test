import random
from random import randint

monString = "Bonjour"
print(monString.rjust(10))

list = [random.randint(1,100) for x in range(10)]
def reverseC(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] > list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp

def reverseD(tab):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] < list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp


reverseC(list)
print(list)
reverseD(list)
print(list)