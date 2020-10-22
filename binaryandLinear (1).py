"""1 create a random list (array) 
2 nrandomize a  search item to be found in the list
3 sequentially search the array for that item.  You must code the search and not use a search function.  
4 Display each comparison in the array; the element contents and the index.
5 display whether the item was found or not.
Now take that code and alter it to have two lists. 

Both lists randomize between 1 and 50. 

While traversing one list, use the linear search to compare each element of list 1 to list 2.

Display the element from the first list and whether it matched the element from the second list.  
later
Perform the a binary search with the same list within the same program.    """ 
import random
num = []
num2 = []

for i in range(20):
  a = random.randrange(1, 50, 1)
  b = random.randrange(1, 50, 1)
  num.append(a)
  num2.append(b)
print("list 1",num)
print("list 2",num2)
print("Linear search:")
for i in range (20):
  for j in range (20):
     if (num[i] == num2[j]):
       print("Element is : ", num[i], " match of 2 lists")
       print("Index list 1: ",i)
       print("Index list 2: ",j)
num.sort()#out
num2.sort()#in
print("list 1",num)
print("list 2",num2)
def bi_search (arr, low, high, x,m):
  if high >= low:
    mid = (high + low )//2
    if arr[mid] == x:
      print("Element is : ", arr[mid], " match of 2 lists")
      print("Index list 1: ",mid+1)
      print("Index list 2: ",m+1)

      return mid
    elif arr[mid] >x:
      return bi_search(arr, low, mid - 1,x,m)
    else:
      return bi_search(arr,mid+1, high, x,m)
  else :
    return -1

def binary_search(arr, arr2):
   print()
   print("Binary search")
   high = 19
   low = 0
   for i in range(20):
     bi_search(arr, low, high, arr2[i],i)
binary_search(num,num2)