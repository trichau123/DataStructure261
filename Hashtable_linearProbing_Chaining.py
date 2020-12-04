
"""
author: tri chau
Linear probing"""
"""Chaining hashtable"""
key = []
print("linear probing")
def display_hash_linear(hashTable):
  for i in range(len(hashTable)):
    print(i, end = " ")

    for j in hashTable[i]:
      print("-->", end = " ")
      print(j, end = " ")

    print()
def display_hash_probing(HashTable):
  for i in range(len(HashTable)):
    print("\n",i,"-->", end = " ")

    for j in HashTable[i]:
      print("", end = "")
      print(j, end = "")
 # function will find the position empty in Hashtable the return
def posEmpty(HashTable):
  count = 0
  for k in HashTable:
    if k == []:
      return count
    count += 1
  return False
#

def posDub(Hashtable):
  for k in Hashtable:
    if k != [] and len(k) > 1:
      HashTable[posEmpty(HashTable)] = k.pop()




   
# Creating hashtable as
# A nested list
HashTable = [[] for _ in range(14)]

#Hasing Function to return
#Key for every value
def Hashing(keyvalue):
  return keyvalue % len(HashTable) #keyvalue mod length of table
#Check dublicate hash key
#insert function to add
#values to the hash hashTable

def insert(Hashtable, keyvalue, value):
  hash_key = Hashing(keyvalue)
  Hashtable[hash_key].append(value)



arr = [[201,"Jill"],[342,"Jim"],[251,"Sandy"],[116,"Sally"],[198,"Ahmed"],[306,"Farhan"],[777,"Theodore"],[823,"Minar"],[921,"Maranda"],[405,"Maribel"],[406,"Leslie"],[528,"Rae"],[233,"John"],[134,"Jessye"]]
for i in range(len(arr)):
  insert(HashTable,arr[i][0],arr[i][1])
#Hash table before Probing
print("Hashtable Chaining Solution:")
display_hash_linear (HashTable)
print("\nHashtable Linear Probing:")
posDub(HashTable)
display_hash_probing(HashTable)


