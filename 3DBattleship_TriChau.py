
import random
arrayBoard = [[[" " for l in range (3)] for i in range (10)] for j in range (10)]
randomLV = 0
def randomF( start, end):
  randomLV = random.randint(start,end)
  return  randomLV

ship1 = [randomF(0,9),randomF(0,9),randomF(0,2)]
ship2 = [randomF(0,9),randomF(0,9),randomF(0,2)]
ship3 = [randomF(0,9),randomF(0,9),randomF(0,2)]
ship4 = [randomF(0,9),randomF(0,9),randomF(0,2)]
ship5 = [randomF(0,9),randomF(0,9),randomF(0,2)]

  # the ships cant hit
if(ship1[2] == ship2[2] or ship1[2] == ship3[2] or ship1[2] == ship4[2] or ship1[2] == ship5[2] or ship2[2] == ship3[2] or ship2[2] == ship4[2] or ship2[2] == ship5[2] or ship3[2] == ship4[2] or ship3[2] == ship5[2] or ship4[2] == ship5[2]):
  while (ship1[0] < 1 or ship1[0] > 7 or ship1[1] < 1 or  ship1[1] >7):
          ship1 = [randomF(0,9),randomF(0,9),randomF(0,2)]
  while (ship2[0] < 2 or ship2[0] > 6 or ship2[1] < 1 or ship2[1] >6):
          ship2 = [randomF(0,9),randomF(0,9),randomF(0,2)]
  while (ship3[0] < 1 or ship3[0] > 6 or ship3[1] < 1 or ship3[1] >6):
          ship3 = [randomF(0,9),randomF(0,9),randomF(0,2)]
  while (ship4[0] < 1 or ship4[0] > 5 or ship4[1] < 1 or ship4[1] >5):
          ship4 = [randomF(0,9),randomF(0,9),randomF(0,2)]
  while (ship5[0] < 1 or ship5[0] > 4 or ship5[1] < 1 or ship5[1] >4):
          ship5 = [randomF(0,9),randomF(0,9),randomF(0,2)]

s1 = 0
s2 = 0
s3 = 0
s4 = 0
s5 = 0
a= 0 
b = 0
c = 0
d = 0
e = 0
#random ship
myShip = [1,2,3,4,5]
random.shuffle(myShip)
a = myShip.pop()
b = myShip.pop()
c1 = myShip.pop()
d = myShip.pop()
e = myShip.pop()
print(a,b,c1,d,e)

def hori(s1,s2,s3,s4,s5):
  for l in range (3):
    for r in range (10):
      for c in range (10):
          if (c == ship1[0] + s1 and r == ship1[1] + s1 and l == ship1[2] ):
                arrayBoard[c][r][l] = str(a) 
                print (arrayBoard[c][r][l], end =" ")
                if(s1 < 1): 
                  s1 += 1
                continue
          if (c == ship2[0] - s2 and r == ship2[1] + s2 and l == ship2[2] ):
                arrayBoard[c][r][l] = str(b)
                print (arrayBoard[c][r][l], end = " ")
                if(s2 < 2): 
                    s2 += 1
                continue           
          if (c == ship3[0] and r == ship3[1] + s3 and l == ship3[2] ): 
                arrayBoard[c][r][l] = str(c1)
                print (arrayBoard[c][r][l], end = " ")
                if(s3 < 2): 
                    s3 += 1
                continue          
          if (c == ship4[0] + s4 and r == ship4[1] + s4 and l == ship4[2] ):
                arrayBoard[c][r][l] = str(d)
                print (arrayBoard[c][r][l],end = " ")
                if(s4 < 3): 
                    s4 += 1
                continue
          if (c == ship5[0] + s5 and r == ship5[1] and l == ship5[2] ):
                arrayBoard[c][r][l] = str(e)
                print (arrayBoard[c][r][l], end = " ")
                if(s5 < 4): 
                    s5 += 1
                continue
          arrayBoard[c][r][l] = "-"
          print (arrayBoard[c][r][l], end = " ")
      print()
    print()

mycode = [hori(s1,s2,s3,s4,s5)]
random.choice(mycode)




