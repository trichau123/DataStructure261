import random
numCups = random.randint(10,20)
cups = [[] for i in range(numCups)]
rounds = 0
balls = 0
bl = True
#while True:
#Throwing phase
while(bl):
    print("\nRound Number :", rounds+1)
    bool = True
    print("Throwing phase")
    a = "Cup,Ball"
    print(a,"",a,"",a," ",a,"",a,"",a," ",a,"")
        # back throwing phase
    i = 0
    # use to count number of ball remain
    a = 0
    for i in range(len(cups)):
        ballNo = random.randint(1, numCups - 1)
        cupNo = random.randint(1, numCups - 1)
        cupNo = i
        if [] in cups:
          #cups[cupNo].insert(0,ballNo)
          cups[cupNo].append(ballNo)
        else:
          if (i != cups[i][0] ):
            x = cups[cupNo].pop(0)
            cups[cupNo].insert(0,ballNo)
          elif(i == cups[i][0]):
            cups[cupNo].append(i)
    for i in range(len(cups)):
        print("|%3d,%5d"%(i,cups[i][0]),end="")
        if (i%7 == 0 ):
          print()

    #pruning phase
    bool2 = True
    print("\nPruning phase")
    a = "Cup,Ball"
    print(a,"",a,"",a," ",a,"",a,"",a," ",a,"")

    i = 0
    # use to count number of ball remain
    a = 0
    c = [1]
    while (bool2):
      for i in range(len(cups)):
        cupNo = i
        ballNo = cups[i][0]
        if (i != cups[i][0]):
          x = cups[cupNo].pop(0)
          cups[cupNo].insert(0,0)
        else:
            a+= 1
          #cups[cupNo].append(0)
        #else:
        # cups[cupNo].insert(cupNo,0)
      bool2 = False
    for i in range(len(cups)):
        if(i>0):
            c.append(cups[i][0])
        print("|%3d,%5d"%(i,cups[i][0]),end="")
        if (i%7 == 0 ):
          print()
    i = 1
    #
    rounds += 1
    # add ballNo
    balls += len(cups) - a

    #for i in range(len(cups)):
      #run from cups[0] to [n] len(cups[n]) = integer 
      #compare len(cups[n]) and len(cups[n+1])
      #if len(cups[n])< len(cups[n+1]) swap cup[n] cup[n+1]
    for i in range(len(cups)):
      if( 0 not in c and i == cups[i][0]):
        #begin to sort
          for n in range(len(cups)):
            min_i = n
            for j in range(n + 1, len(cups)):
              if len(cups[min_i]) < len(cups[j]):
                min_i = j 
            cups[n], cups[min_i] = cups[min_i],cups[n]
            #finish
          print("\nAfter sort decending order")
          a = "Cup,Ball"
          print(a,"",a,"",a," ",a,"",a,"",a," ",a,"")
          for n in range(len(cups)):
            print("|%3d,%5d"%(cups[n][0],cups[n][0]),end="")
            if (n%7 == 0 ):
              print()
          print("\nRound ", rounds)
          print("\nBalls ", balls)
          bl =  False
          break 
    
#TriHuynhChau
          
    
  



