'''
def cipher(word:str,a:int,key:int)->str:
  scrambledWord = ""
  for lett in word:
    newLett = ord(lett)
    #(letter + key)%26
    newLett = ((a*newLett + key-65)%26+65)
    print(newLett-65)
    scrambledWord += chr(newLett)
  return scrambledWord

def deCipher(word:str,a:int,key:int)->str:
  scrambledWord = ""
  for lett in word:
    newLett = ord(lett)
    #print(newLett)
    newLett = ((a*newLett - key-65)%26+65)
    print(newLett-65)
    scrambledWord += chr(newLett)
  return scrambledWord

for lett in "QUIZ":
  print(ord(lett)-65)
print("QUIZ")

x = cipher("QUIZ",3,4)
print(x)

x = deCipher(x,3,16)
print(x)
'''