import winsound, string, time
def sndDot():
	Freq = 750
	Dur = 200
	winsound.Beep(Freq, Dur)
def sndDash():
	Freq = 750
	Dur = 600
	winsound.Beep(Freq, Dur)
def sndSpace():
	Freq = 50
	Dur = 750
	winsound.Beep(Freq, Dur)
def getText():
	text = input ("Enter a English sentence to convert to Morse Code:")
	changeIn = text.lower()
	print(changeIn)
	return changeIn

caDic = {'a':'._','b':'_...','c':'_._.','d':'_..','e':'.','f':'.._.','g':'__.','h':'....','i':'..','j':'.___','k':'_._','l':'._..','m':'__','n':'_.','o': '___','p':'.__.','q':'__._','r':'._.','s':'...','t':'_','u':'.._','v':'..._','w':'.__','x':'_.._','y':'_.__','z':'__..','.':'._._._',',':'__..__','?':'..__..','/':'_.._.','@':'.__._.','1':'.____','2':'..___','3':'...__','4':'...._','5':'.....','6':'_....','7':'__...','8':'___..','9':'____.','0':'_____'}
txt = getText()# Chau Huynh Tri
splText = txt.split()#["chau","huynh","tri"]
def separCha():
  ca = []
  for i in range(len(splText)):
    splCharacter = splText[i]
    ca.append(splCharacter)
  a = list(map(list,ca))
  print(a)
  return a
listCa = separCha()
def morsels():
  morse = []
  for i in range (len(listCa)):
    for j in range(len(listCa[i])):
      x = caDic.get(listCa[i][j])
      if (x):
        morse.append(x)
    print()
  print(morse)
  return morse
soundf = morsels()
def stringSoundEff(soundf):
  strSound = ""
  for i in range(len(soundf)):
    for j in range(len(soundf[i])):
      strSound += soundf[i][j]
    strSound += " "
  return strSound
strSound = stringSoundEff(soundf)
def soundEff(strSound):
  for i in range(len(strSound)):
      if(strSound[i] == "_"):
        sndDash()
      elif(strSound[i] == "."):
        sndDot()
      elif(strSound[i] == " "):
        sndSpace()
  
soundEff(strSound)
