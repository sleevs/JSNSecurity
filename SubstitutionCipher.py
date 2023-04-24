import random


print("\n")
print("SUBSTITUTION CIPHER")



def genereteKey():
   
    letters = "ABCDEFGHIJkLMNOPQRSTUVWXYZ"
    cletters = list(letters)
    key = {}
    cnt = 0 
    for c in letters:
        key[c] = cletters.pop(random.randint(0,len(cletters) - 1))
        cnt += 1
    return key




key = genereteKey()
print("--- key --- \n")
print(key)
print("\n")




def encrypt(key , message):
    
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher



message = "LUIZ GAMA"
cipher = encrypt(key, message)
print("--- ENCRYPR MESSAGE --- \n")
print(cipher)
print("\n")




def decrypt(key):
    
    dkey={}
    
    for k in key:
        dkey[key[k]] = k
        
    return dkey




dkey = decrypt(key)
message = encrypt(dkey,cipher)
print("--- DECRYPT  MESSAGE --- \n")
print(message)
print("\n")



    