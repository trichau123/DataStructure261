"""You will create a program that will follow the queuing theory of the Barbershop Problem.  You will initially create a flow chart for the assignment to be uploaded to the Queuing Theory Flowchart assignment drop box.  In this you will use queues and random number generators to complete this project.  You will create three queues

Couch - the area where patron will wait just prior to getting their hair cut;
Line - the area where patron will form a line just before reaching the couch; and
Cashier - the area where patrons will line up to pay just before exiting the barbershop and after finishing their haircut.  
You will create a container for the barbers chairs (list) .  The wait times for the barbers will be random.  Barber one will be the fastest and barber three will be the slowest.  Randomize the wait times accordingly.  

The cashier wait times will also vary randomly.

Barber wait times.

1 second (system time) = 5 minutes
Max time 2 hours // 24 second
Min time 20 minutes.//4 second
Cashier wait time 

1 second (system time) = 1 minute
Max time 3 minutes / 3 
Min time 1 minute."""

import time, random

count = 0
line = []
couch = []
cashiers = []
#welcome people to barber
while(count<15):
  line.append(count)
  count += 1
while(len(line) > 0):
  print("************************")
  #len line > 0
  print("People on the line ",line)
  count = 0
  while( count < 3):
    if(len(line)>0):
      couch.append(line.pop(0))
      print("Couch number",count + 1," : ",couch)
    count += 1
  #Couch
  print("Baber couches  ",couch)
  def waitTime(b):
    btime = 0
    a = time.time() 
    while (btime <b):
      btime = time.time() - a
  b1 = random.randint(4,24)
  b2 = random.randint(0,b1)
  b3 = random.randint(0,b2)
  if(len(couch)== 3):
    print("Waiting Time for couches :", b1*5," minutes",b2*5+b1*5," minutes",b3*5+b1*5 + b2*5," minutes")
  elif(len(couch)==2 ):
    print("Waiting Time for couches :", b1*5," minutes",b2*5+b1*5," minutes")
  else:
    print("Waiting Time for barbers to finish :", b1*5," minutes")
  print("Waiting.....")
  print("No one check out now : ", cashiers)
  cashiers.append(couch.pop(0))
  waitTime(b1)
  print("Customer finish haircut: ",cashiers[0])
  if(len(couch)>0):
    cashiers.append(couch.pop(0))
    waitTime(b2)
    print("Customer finish haircut: ",cashiers[1]," " , cashiers)
  if(len(couch)>0):
    cashiers.append(couch.pop(0))
    waitTime(b3)
    print("Customer finish haircut: ",cashiers[2]," " , cashiers)
  while(len(cashiers)>0):
    print("Line waiting for checkout: ", cashiers)
    print("Finish checkout customer: ",cashiers[0]," " , cashiers)
    cashiers.pop(0)
    waitTime(random.randint(1,3))
    print("Cashiers waiting : ", cashiers)
print("No more customer, Closed !!!")
    