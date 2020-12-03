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


arr = [[201,"Jill"],[342,"Jim"],[251,"Sandy"],[116,"Sally"],[198,"Ahmed"],[306,"Farhan"],[777,"Theodore"],[823,"Minar"],[921,"Maranda"],[405,"Maribel"],[406,"Leslie"],[528,"Rae"],[233,"John"],[134,"Jessye"]]
for i in range(len(arr)):
  insert(HashTable,arr[i][0],arr[i][1]) 
display_hash (HashTable) 

