caDic = {'a':'._','b':'_...','c':'_._.','d':'_..','e':'.','f':'.._.','g':'__.','h':'....','i':'..','j':'.___','k':'_._','l':'._..','m':'__','n':'_.','o': '___','p':'.__.','q':'__._','r':'._.','s':'...','t':'_','u':'.._','v':'..._','w':'.__','x':'_.._','y':'_.__','z':'__..','.':'._._._',',':'__..__','?':'..__..','/':'_.._.','@':'.__._.','1':'.____','2':'..___','3':'...__','4':'...._','5':'.....','6':'_....','7':'__...','8':'___..','9':'____.','0':'_____'}
txt = getText()# ._ _... _._.
splText = txt.split()#["._","_...","_._."]
def getText():
	text = input ("Enter Morse Code to convert to English Character:")
	return text


def get_key(val):
  for key, value in caDic.items():
      if val == value:
          return key
  return "key not exist"

#create an array of characters
def arrchar():
  arc = []
  for i in range (len(splText)):#[[].[].[]]
      x = get_key(splText[i])
      if (x):
        arc.append(x)
  return arc 
soundf = arrchar()
#add array to string
def stringChar(soundf): 
  strChar = ""
  for i in range(len(soundf)):
    for j in range(len(soundf[i])):
      strChar += soundf[i][j]
    strChar += " "
  return strChar # string
strChar = stringChar(soundf)

  
print(strChar)
