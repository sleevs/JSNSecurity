def generate_key(n):
    letters = "ABCDEFGHIJkLMNOPQRSTUVWXYZ"
    key = {}
    cnt = 0 
    for c in letters:
        key[c] = letters[(cnt + n) % len(letters)]
        cnt += 1
    return key


def encrypt(key , message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher



def get_decrypt_key(key):
    dkey = {}
    for c in key:
        dkey[key[c]] = c
    return dkey



key = generate_key(10)
print(key)
message = "JEISON"
#message = "GIANT HORSES"
cipher = encrypt(key, message)
print(cipher)

dkey = generate_key(26-10)
message = encrypt(dkey, cipher)
print(message)

s = get_decrypt_key(key)
print("==================")
print(s)


for i in range(26):
    dkey = generate_key(i)
    message = encrypt(dkey, cipher)
    print(message)