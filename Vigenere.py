# Persians: Sydney Anderson, Tram Doan, Devon Knudsen, Zackary Phillips, Promyse Ward, James Wilson
# GitHub Repo: https://github.com/devonknudsen/Vigenere-Cipher
# Written in Python 3.7

import sys
import enum
import string

# encrypts pain text to cipher text
def Cipher(plainText, key):
    P = list(plainText)
    K = list(key)
    C = [] * len(plainText)
    x = 0
    
    # iterate through each index in the plain text
    for i in range(0, len(P)):
    
        # x is used to track and repeat key
        # when x reaches the key's length, it resets
        if (x == len(K)):
            x = 0
            
        # checks if the letter of the plain text is an alphabetic character
        # if true: find and add integer value
        if (P[i].isalpha()):
            Pi = ASCIIValue(P[i])
            Ki = ASCIIValue(K[x])
            c_int = (Pi + Ki)%26
            x+= 1
            
        # else: add symbol/numerical value
        else:
            c_int = P[i]

        C.append(c_int)

    return C
    
# decrypts cipher text to plain text
def Decipher(cipherText, key):
    C = list(cipherText)
    K = list(key)
    P = [] * len(cipherText)
    x = 0

    # iterate through each index in the cipher text
    for i in range(0, len(C)):
        
        # x is used to track and repeat key
        # when x reaches the key's length, it resets
        if (x == len(K)):
            x = 0
            
        # checks if the letter of the cipher text is an alphabetic character
        # if true: find and add integer value     
        if (C[i].isalpha()):
            Ci = ASCIIValue(C[i])
            Ki = ASCIIValue(K[x])
            p_int = (Ci - Ki + 26)%26
            x += 1
            
        # else: add symbol/plainTextList value
        else:
            p_int = C[i]

        P.append(p_int)

    return P

# returns the number value of a letter
def ASCIIValue(letter):

    # if the letter is lowercase, get lowercase alphabet
    if letter.islower():
        alphabet = list(string.ascii_lowercase)
        
    # else, get uppercase alphabet
    else:
        alphabet = list(string.ascii_uppercase)
    
    # find letter in alphabet
    for i in range(len(alphabet)):
        if (alphabet[i] == letter):
            return i
        
# returns the letter value of a number
def CharValue(int, case):

    # if the letter was once uppercase, get lowercase alphabet
    if case == True:
        alphabet = list(string.ascii_lowercase)
        
    # else, get uppercase alphabet
    else:
        alphabet = list(string.ascii_uppercase)
        
    # return letter in alphabet
    return alphabet[int]


# MAIN CODE #

# remove spaces from key (can also be done in cipher/decipher functions)
key = sys.argv[2]
key = key.replace(" ", "")

# if want to encrypt a plain text
if (sys.argv[1] == "-e"):
    
    while(True):

        # used try, except to prevent keyboardInterruption error thrown
        try:
            cipherText = ""
            plainText = input()
            plainTextList = list(plainText)
            
            # encipher plain text into a list of integers
            intList = Cipher(plainText, key)
            
            
            # convert each integer into it's mapped letter of the alphabet
            for i in range(0, len(intList)):
            
                # check if the object is an integer
                # if so, convert to letter
                if(isinstance(intList[i], int)):
                    cipherText += str(CharValue(intList[i], plainTextList[i].islower()))
                
                # else, add symbol/numerical value
                else: 
                    cipherText += intList[i]

            print(cipherText)
            
        except KeyboardInterrupt:
        # this will exit if the user does ^d, or ^z, ^c, or whatever their system's exit is
            sys.exit(1)

        # this will catch the EOF error (EOF - End of file)
        # we're getting this error because we're not using stdin    
        except EOFError:
            break

      
# if want to decrypt a cipher text      
elif (sys.argv[1] == "-d"):
    while(True):
        # used try, except to prevent keyboardInterruption error thrown
        try:
            plainText = ""
            cipherText = input()
            plainTextList = list(cipherText)
            
            # decipher cipher text into a list of integers
            intList = Decipher(cipherText, key)
            
            # convert each integer into it's mapped letter of the alphabet
            for i in range(0, len(intList)):
            
                # check if the object is an integer
                # if so, convert to letter
                if(isinstance(intList[i], int)):
                    plainText += str(CharValue(intList[i], plainTextList[i].islower()))
                
                # else, add symbol/numerical value
                else:
                    plainText += intList[i
]
            print(plainText)

        except KeyboardInterrupt:
        # this will exit if the user does ^d, or ^z, ^c, or whatever their system's exit is
            sys.exit(1)

        # this will catch the EOF error (EOF - End of file)
        # we're getting this error because we're not using stdin    
        except EOFError:
            break
