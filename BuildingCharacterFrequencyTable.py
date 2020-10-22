import random, string
aAlphabet = list(string.ascii_lowercase)
dCharCnt = {}
cnt = 0
strEncrypt = "".join([random.choice(aAlphabet)for strChar in range(45)])
splText = strEncrypt.split()
caDic = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o': 0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}

def separCha():
  ca = []
  for i in range(len(splText)):
    splCharacter = splText[i]
    ca.append(splCharacter)
  a = list(map(list,ca))
  return a
listCa = separCha()
for i in range (len(listCa[0])):
  ca = listCa[0][i]
  for key, value in caDic.items():
      if key == ca and value == 0 :
        value = 1
        caDic.update({key:value})
      elif key == ca :
        value += 1
        caDic.update({key:value})
print("list before: ",splText)

for key, value in caDic.items():
      if value != 0 :
        print(key ,":" , value)
print("list after",caDic)
