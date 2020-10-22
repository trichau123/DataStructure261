import random
arrayA = [[[" " for l in range (3)] for i in range (4)] for j in range (4)]
for l in range (3):
  for r in range (4):
    for c in range (4):
      arrayA[c][r][l] = str(l)+","+str(r)+"," +str(c)
      print (arrayA[c][r][l], end ="|")
  print()
print()
     



