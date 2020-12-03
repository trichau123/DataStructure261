def display_hash(hashTable):
  for i in range(len(hashTable)):
    print(i, end = " ")

    for j in hashTable[i]:
      print("-->", end = " ")
      print(j, end = " ")

    print()
  
# Creating hashtable as
# A nested list
HashTable = [[] for _ in range(10)]

#Hasing Function to return
#Key for every value
def Hashing(keyvalue):
  return keyvalue % len(HashTable) #keyvalue mod length of table

#insert function to add
#values to the hash hashTable
def insert(Hashtable, keyvalue, value):
  hash_key = Hashing(keyvalue)
  Hashtable[hash_key].append(value)


arr = [["Bryce Harper","0.336735"],["Christian Yelich","0.311321"],["Francisco Cervelli","0.315068"],["Gleyber Torres","0.242105"],["Jean Segura","0.315217"],["Mike Zunino","0.186667"],["Mookie Betts","0.347368"],["Trevor Story","0.291262"]]
for i in range(len(arr)):
  letters = arr[i][0]
  numbers = [ord(letter) for letter in letters]
  a = 0
  for j in range(len(numbers)):
    a += numbers[j]
  insert(HashTable,a,arr[i][1]) 
display_hash (HashTable) 
