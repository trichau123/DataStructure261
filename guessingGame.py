
import random
from random import randint

arrayBoard = ["" for j in range (300)]
randomLV = randint(1,300)
count = 0
for i in range(300):
    arrayBoard[i] = i+1
#print
def prnt(arrayBoard):
    a = ""
    for i in range(300):
        a = a + " " + str(arrayBoard[i])
        if((i+1) == 25 or (i+1) == 50 or (i+1) == 75 or (i+1) == 100 or (i+1) == 125 or (i+1) == 150 or (i+1) == 175 or (i+1) == 200 or (i+1) == 225 or (i+1) == 250 or (i+1) == 275 or (i+1) == 300):
            a = a + "\n"
    print(a)
prnt(arrayBoard)
print("random number is :",randomLV)
#find x
def bina(arr, x):
    low = 0 
    high = len(arr) - 1
    mid = 0
    
    while low <= high:
        mid = (high + low )//2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
#function print x
def find(pos, arr, x):
    for i in range(300):
        if (x >=151 and i >= 150):
            arr[i] = i+1
        elif (x <=150 and i <= 149):
            arr[i] = i+1
        else:
            arr[i] = "X"
    prnt(arr)
    print("")
    for i in range(300):
        if(pos  == i):
            arr[i] = pos + 1
        else:
            arr[i] = "X"
    prnt(arr)    
pos = bina(arrayBoard,randomLV)
find(pos, arrayBoard,randomLV)







