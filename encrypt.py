import unicodedata
import re
import numpy

def onlyAlpha(S):
    if type(S) is str:
        tempList = S
    else:
        tempList = ''.join(S)

    tempList = re.sub(r'\W+', '', tempList)
        
    tempList = list(unicodedata.normalize('NFKD', tempList).encode('ASCII', 'ignore').decode("utf-8").upper())
         
    return tempList

def charToNumb(S):
    tempList = S
    var = {'A':'0','B':'1','C':'2','D':'3','E':'4',
           'F':'5','G':'6','H':'7','I':'8','J':'9',
           'K':'10','L':'11','M':'12','N':'13','O':'14',
           'P':'15','Q':'16','R':'17','S':'18','T':'19',
           'U':'20','V':'21','W':'22','X':'23','Y':'24',
           'Z':'25'}

    for i,char in enumerate(tempList):
        tempList[i] = var[char]
        
    
    return tempList

def numbToChar(S):
    tempList = S

    var = {'A':'0','B':'1','C':'2','D':'3','E':'4',
           'F':'5','G':'6','H':'7','I':'8','J':'9',
           'K':'10','L':'11','M':'12','N':'13','O':'14',
           'P':'15','Q':'16','R':'17','S':'18','T':'19',
           'U':'20','V':'21','W':'22','X':'23','Y':'24',
           'Z':'25'}
    var = {v: k for k, v in var.items()}

    for i,char in enumerate(tempList):
        tempList[i] = var[str(char)]

        
    return tempList

def cesar(S,n):
    tempList = charToNumb(onlyAlpha(S))
    for i,elt in enumerate(tempList):
        tempList[i] = (int(tempList[i])+n)%26

    tempList = numbToChar(tempList)
    
    return tempList

def vigenere(S,c):
    tempList = charToNumb(onlyAlpha(S))
    c = onlyAlpha(c)

    var = {'A':'0','B':'1','C':'2','D':'3','E':'4',
           'F':'5','G':'6','H':'7','I':'8','J':'9',
           'K':'10','L':'11','M':'12','N':'13','O':'14',
           'P':'15','Q':'16','R':'17','S':'18','T':'19',
           'U':'20','V':'21','W':'22','X':'23','Y':'24',
           'Z':'25'}
    
    for i,elt in enumerate(tempList):
        tempList[i] = (int(tempList[i])+int(var[c[i%len(c)]]))%26

    tempList = numbToChar(tempList)

    return tempList

def enigma(S,t,r,f):

    pass


def listLetters(S):
    S = onlyAlpha(S)
    tempDict = {'A':'0','B':'0','C':'0','D':'0','E':'0',
                'F':'0','G':'0','H':'0','I':'0','J':'0',
                'K':'0','L':'0','M':'0','N':'0','O':'0',
                'P':'0','Q':'0','R':'0','S':'0','T':'0',
                'U':'0','V':'0','W':'0','X':'0','Y':'0',
                'Z':'0'}

    for i,char in enumerate(S):
        tempDict[char] = int(tempDict[char])+1
        
    return tempDict

def frequenceLetters(S):
    message = onlyAlpha(S)
    tempDict = listLetters(S)

    for elt in tempDict:
        tempDict[elt] = float(tempDict[elt])/len(message)

        
    return tempDict

def percentLetters(S):
    message = onlyAlpha(S)
    tempDict = listLetters(S)

    for elt in tempDict:
        tempDict[elt] = float(tempDict[elt])/len(message)*100

    return tempDict

stra = "Ce méssage est secret !"


print(percentLetters(stra))
