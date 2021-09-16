import random
import string
#create the number of cups from 1 to ...
random_Cups = random.randint(1, 10)
#create 2 dimension array to contain cups

cups = [[] for i in range(random_Cups)]
# varible for the game keep going
bl = True
count = 0
while bl:
  if [] in cups:
    def createBall():
        ball = random.randint(0, random_Cups-1)
        return ball

    #a = randomCups()

    # create the list of cups' lable
    cup_num = list(range(0, random_Cups))

    # shuffle cups lables 
    random.shuffle(cup_num)

    #Throwing phase
    print("Throwing phase")
    boolean = True
    j = 0
    while (boolean):
      for i in range (len(cup_num)):
        cups[cup_num[i]].append(createBall())
      else:
        boolean = False
    print(cups)
    #Prunning phase 
    print("Prunning Phase")
    for i in range (len(cup_num)):
      for j in range (len(cups[i])):
        if i != cups[i][j] :
          cups[i].pop(j)
    print(cups)
    bl = True
# else exit while    
    count += 1
  else:
    bl = False
#total Ball to count how many balls in all the cups
ttBall = 0
for i in range (random_Cups):
  for j in range (len(cups[i])):
    ttBall += 1
print("Total : ", count, " Game.")
print("Total Ball: ", ttBall)

