import operator
import sys

cipher = """ QWOPEIRRYEWRP OIYRPO   IWEYRPOITYUIQOIUEYRGFASJHDF 
LJH FKDG BMZXNCBV MXNCVBMXZMMN AADFD GHJKL QWQERTRRE TYUUIOPGDF"""


def decrypt(key, cipher):
    
    message = ""
    for c in cipher:
        if c in key:
            message += key[c]
        else:
            message += c
    
    return message



class Attack:
    
    
    def __init__(self) -> None:
        self.alphabet = "ABCDEFGHIJkLMNOPQRSTUVWXYZ"
        self.freq= {}
        self.mappings = {}
        self.key = {}
        self.frequency = {'A' : 0.03,'B' : 0.03,'C' : 0.02,'D' : 0.05,'E' : 0.06,'F' : 0.05,'G' : 0.04,'H' : 0.03,'I' : 0.07,'J' : 0.03,'k' : 0.0,'L' : 0.02,'M' : 0.05,'N' : 0.03,'O' : 0.06,'P' : 0.05,'Q' : 0.04,'R' : 0.09,'S' : 0.01,'T' : 0.03,'U' : 0.04,'V' : 0.02,'W' : 0.04,'X' : 0.03,'Y' : 0.06,'Z' : 0.02,           }
        self.plainCharLeft = "ABCDEFGHIJkLMNOPQRSTUVWXYZ"
        self.cipherCharLeft = "ABCDEFGHIJkLMNOPQRSTUVWXYZ"




    def getKey(self):
        return self.key
    
    """
    give: cipher
    when: alphabet
    then: frequency is
    """
    def claculateFrquency(self, cipher):
        for f in self.alphabet:
            self.freq[f] = 0
            
            
        count = 0
        for c in cipher:
            if c in self.freq:
                self.freq[c] += 1
                count +=1


        for f in self.freq:
            self.freq[f] = round(self.freq[f]/count,4)
    
    
    
    def printFrequency(self):
        count_2 = 0 
        for f in self.freq:
            print(f , ':', self.freq[f] , end=',')
            if count_2 % 3 == 2:
                print()
                count_2 += 1
                
                
    
        """
    give: alphabet
    when: frequency in cipher
    then:  mappings frequency is
    """     

    def calculateMatches(self):
        
        for cipherChar in self.alphabet:
            map = {}
            for plainChar in self.alphabet:
                map[plainChar] = round(abs(self.freq[cipherChar] - self.frequency[plainChar]),4)
            self.mappings[cipherChar] = sorted(map.items() , key=operator.itemgetter(1))   
            
            
     
    """
    give: cipherCharLeft AND mappings
    when: frequency in cipher
    then:  KEY is
    """     
           
    def guessKey(self):
        
        key = {}
        for cipherChar in self.cipherCharLeft:
            for plainChar , diff in self.mappings[cipherChar]:
                if plainChar in self.plainCharLeft:
                    key[cipherChar] = plainChar
                    self.plainCharLeft = self.plainCharLeft.replace(plainChar,'')
                    break            
        return  key
    
    
    def setKeyMapping(self , cicpherChar , plainChar):
        
        if cicpherChar not in self.cipherCharLeft or plainChar not in self.plainCharLeft:
            
            print("ERRO KEY MAPPING ERRO" , cicpherChar , plainChar)
            sys.exit(-1)
            
        
        self.key[cicpherChar] = plainChar
        self.plainCharLeft = self.plainCharLeft.replace(plainChar , '')
        self.cipherCharLeft = self.cipherCharLeft.replace(cicpherChar,"")

        
        
   






print()
print(" -- GENERATE FREQUENCY -- \n")

attack = Attack()
attack.claculateFrquency(cipher)
attack.printFrequency()
print("\n")




print(" -- GENERATE MATCHES IN FREQUENCY -- \n")
attack.calculateMatches()

for result in attack.mappings:
    print(result , attack.mappings[result])
    


attack.setKeyMapping('F','D')
attack.setKeyMapping('E','E')
attack.setKeyMapping('G','F')
attack.setKeyMapping('Q','G')
attack.setKeyMapping('A','H')
attack.setKeyMapping('Y','I')
attack.setKeyMapping('B','J')
attack.setKeyMapping('k','k')
attack.setKeyMapping('P','M')
attack.setKeyMapping('N','O')




    

    
print("\n")
print(" -- GENERATE GUESS KEY -- ")
key = attack.guessKey()
print(key)





print("\n")
print(" -- GENERATE GUESS MESSAGE -- ")
message = decrypt(key, cipher)

messageLines = message.splitlines()
cipherLine = cipher.splitlines()

for i in range(len(messageLines)):
    print('TEXTE :' , messageLines[i])
    print('CIPHER :' , cipherLine[i])
