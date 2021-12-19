def cipher(word:str,key:int)->str:
  scrambledWord = ""
  for lett in word:
    newLett = ord(lett)
    newLett = ((newLett + key-65)%26+65)
    print(newLett-65)
    scrambledWord += chr(newLett)
  return scrambledWord

def deCipher(word:str,key:int)->str:
  scrambledWord = ""
  for lett in word:
    newLett = ord(lett)
    #print(newLett)
    newLett = ((newLett - key-65)%26+65)
    print(newLett-65)
    scrambledWord += chr(newLett)
  return scrambledWord

x = cipher("TEST",16)
print(x)

x = deCipher(x,16)
print(x)
