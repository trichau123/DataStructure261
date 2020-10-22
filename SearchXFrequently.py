"""Create an array of the numbers one through ten .
Shuffle those numbers.
Randomly pick a number between one and ten and then sequentially search the array for that number.
Once the number is found, place that number at the from of the list.
Print the list
Perform #3 thru #5 ten times.   """
import random
count = 0
while(count<6):
  print("\n*****************\nThe list random value")
  a = [1,2,3,4,5,6,7,8,9,10]
  random.shuffle(a)
  print(a)
  num = random.randint(1,10)
  print(num)
  pos = 0
  for i in range(len(a)):
    if(num == a[i]):
      pos = i
      print("POSITION OF NUM : ", i)
  print(pos)
  a.pop(pos)
  a.insert(0,num)
  print(a)
  count += 1
#Tri Chau
