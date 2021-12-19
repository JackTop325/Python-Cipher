def cipher(word:str,key:int)->str:
    """cipher function

    The cipher function will encode the given word using the given key

    Args:
        word (str): the string word or phrase
        key (int): the key that will shift the word

    Returns:
        str: the new scrambledWord
    """
    scrambledWord = ""
    for lett in word:
        newLett = ord(lett)
        newLett = ((newLett + key-65)%26+65)
        #print(newLett-65)
        scrambledWord += chr(newLett)
    return scrambledWord

def deCipher(word:str,key:int)->str:
    """deCipher function

    The decipher function will decode the given word using the given key

    Args:
        word (str): the string word or phrase
        key (int): the key that will shift the word

    Returns:
        str: the new scrambledWord
    """
    scrambledWord = ""
    for lett in word:
        newLett = ord(lett)
        newLett = ((newLett - key-65)%26+65)
        #print(newLett-65)
        scrambledWord += chr(newLett)
    return scrambledWord
    
def main():
    #Obtain input
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

if __name__ == "__main__":
    main()