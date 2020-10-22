import random 
dCardNames = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
dCardValues = ['2','3','4','5','6','7','8','9','10','11','12','13','14']
dSuits = ["Clubs","Spades","Diamonds","Hearts"]
# Build a two dimensional deck with Cards suits and values.
aCards =  [['' for i in range(52)] for j in range(4)]
i = 0
j = 0
n = 0
while i < 13:
    aCards[0][i] = dCardNames[i]
    aCards[0][i + 13] = dCardNames[i]
    aCards[0][i + 26] = dCardNames[i]
    aCards[0][i + 39] = dCardNames[i]
    aCards[1][i] = dSuits[0]
    aCards[1][i + 13] = dSuits[1]
    aCards[1][i + 26] = dSuits[2]
    aCards[1][i + 39] = dSuits[3]
    aCards[2][i] = dCardValues[i]
    aCards[2][i + 13] = dCardValues[i]
    aCards[2][i + 26] = dCardValues[i]
    aCards[2][i + 39] = dCardValues[i]
    i = i + 1 


#add 2d array to 1d array
newArr = []
print("Array before suffle")
while j < 52:
    # assign value to new array
    newArr.append(aCards[0][j]+ " "+ aCards[1][j]+ " "+ aCards[2][j]+" "+str(j))
    print (aCards[0][j], " ", aCards[1][j], " ", aCards[2][j], " "," index: ",str(j))
    j = j + 1
j =0
#tranform back to 2d array
#add index to dic
a = []
dic = {}
for i in range (52):
  a.append(newArr[i].split(" "))
  dic[i] = a[i]


# shuffle array a
random.shuffle(a)
print("")
print("New Array After Suffle")
def printArray(a):
  print("**************************************")
  j = 0
  while j < 52:
    print("Card name: ",a[j][0]," ",a[j][1], " ", a[j][2])
    j = j + 1
  j = 0 
print("")
card = []

#pick 5 card function
def pick5Card(a):
  card = []
  j = 0
  print("Pick 5 random cards :")
  while j < 5:
    num = random.randint(0 , 52)
    card.append(a[num])
    print("Card ",j+1,": ",a[num][0]," ",a[num][1]," ",a[num][2])
    print("Index ", num)
    j = j + 1
  return card

#selectio sort
def selSort(a):
  print ("Selection sort: ")
  j = 0
  i = 0
  for i in range(len(a)): 
      # Find the minimum element in remaining  
      # unsorted array 
      min_idx = i 
      for j in range(i+1, len(a)): 
          if int(a[min_idx][3]) > int(a[j][3]): 
              min_idx = j 
                
      # Swap the found minimum element with  
      # the first element         
      a[i], a[min_idx] = a[min_idx], a[i] 
#print array after shuffle
printArray(a)

#pick 5 card
card = pick5Card(a)

# selection sort
selSort(a)

#print array 
printArray(a)
#print 5 card after sorted
print("Index of 5 cards after sort:")
for d in range (5):
  print("Card ",d+1,": ",card[d][0]," ",card[d][1]," ",card[d][2])
  print("Index ", card[d][3])
  
#Reshuffle and apply the insertion and selection sort. 

#print array after shuffle again
def insertionSort(a): 
    print("Insertion sort: ")
    # Traverse through 1 to len(arr) 
    for i in range(1, len(a)):  
        key = int(a[i][3])
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and int(a[j][3]) > key : 
                a[j+1], a[j] = a[j], a[j+1] 
                j -= 1

#insertionSort(a)
#printArray(a)
random.shuffle(a)
printArray(a)
#bubble sort
def bubbleSort(a): 
    print("Bubble sort: ")
    n = len(a) 
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if int(a[j][3]) > int(a[j+1][3]) : 
                a[j], a[j+1] = a[j+1], a[j] 

bubbleSort(a)
printArray(a)

def insertion_sort(a):

    # We start from 1 since the first element is trivially sorted
    print("Insertion sort")
    for i in range(1, len(a)):
        currentValue = a[i]
        position = i
        while position > 0 and a[position - 1][3] > a[position][3]:
            a[position] = a[position -1]
            position = position - 1
            a[position] = currentValue
random.shuffle(a)
printArray(a)

insertionSort(a)
printArray(a)