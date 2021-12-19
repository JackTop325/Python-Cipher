def cipher(word:str,key:int)->str:
  scrambledWord = ""
  for lett in word:
    newLett = ord(lett)
    newLett = ((newLett + key-65)%26+65)
    #print(newLett-65)
    scrambledWord += chr(newLett)
  return scrambledWord

def deCipher(word:str,key:int)->str:
  scrambledWord = ""
  for lett in word:
    newLett = ord(lett)
    newLett = ((newLett - key-65)%26+65)
    #print(newLett-65)
    scrambledWord += chr(newLett)
  return scrambledWord

print("Cipher: ")
print("Would you like to use a Cipher(1) or Decipher(2): ")
option = input()
if(option == "1" or option == "Cipher"):
    word = input("Please enter the word: ")
    key = int(input("Please enter the key: "))
    print(f"The new word is: {cipher(word,key)}")
elif(option == "2" or option == "Decipher"):
    word = input("Please enter the word: ")
    key = int(input("Please enter the key: "))
    print(f"The new word is: {deCipher(word,key)}")
else:
    print("I'm not sure what you entered")