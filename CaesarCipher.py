#This program allows the user to encode or decode a Caesar cipher shifted by a given degree

lowerCase = { 1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k',
        12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 
        22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}
upperCase = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 11:'K',
        12:'L', 13:'M', 14:'N', 15:'O', 16:'P', 17:'Q', 18:'R', 19:'S', 20:'T', 21:'U', 
        22:'V', 23:'W', 24:'X', 25:'Y', 26:'Z'}
#dictionary that passes the lowerCase and upperCase dictionaries into the translation functions
dic = {}
#dictionary that holds the translated lowerCase and upperCase dictionaries for a given shift value
cipherDict = {}
encodeList = ['e', 'E', 'encode', 'Encode', 'ENCODE']
decodeList = ['d', 'D', 'decode', 'Decode', 'DECODE']
yesList = ['y', 'Y', 'yes', 'Yes', 'YES']
noList = ['n', 'N', 'no', 'No', 'NO']

#matches each letter in the alphabet with it's shifted counterpart and stores the updated values in the dictionary cipherDict
def Shifter(dic):
    for index, value in dic.items():
        if processCipher in encodeList:
            if (index + shiftNum) > 25:
                newIndex = abs(index + shiftNum) - 25
            else:
                newIndex = index + shiftNum
        else:
            if (index - shiftNum) < 1:
                newIndex = 25 - abs(index - shiftNum)
            else:
                newIndex = index - shiftNum
        newValue = dic[newIndex]   
        cipherDict[value] = newValue

#encrypts or decrypts a user entry by a user defined shift amount
def Encrypter(userCipher):
    dic = lowerCase
    Shifter(dic)
    dic = upperCase
    Shifter(dic)
    print("Decoding at C =", str(shiftNum) + ":", userCipher)
    userCipher = userCipher.split()
    splitCipher = list(map(list,userCipher))
    for index, word in enumerate(splitCipher):
        for idx, letter in enumerate(word):
            if letter in cipherDict:
                if processCipher in encodeList:
                    for key, value in cipherDict.items():
                        if letter == value:
                            word[idx] = cipherDict[value]
                else:
                    word[idx] = cipherDict[letter]
            else:
                continue
        splitCipher[index] = "".join(map(str, word))
    splitCipher = " ".join(map(str, splitCipher))
    if processCipher in encodeList:
        print("Cipher encoded as:", splitCipher)
    else:
        print("Cipher decoded as:", splitCipher)

#main loop
while True:
    #asks user to set the program to encode or decode a user entry
    while True:
        processCipher = input("Enter 'e' to encode a Caesar cipher, or 'd' to decode one. (e/d): ")
        if len(processCipher) < 1:
            processCipher = 'e'
            print("Default selected: Encode")
        elif processCipher in encodeList:
            print("Encode selected")
        elif processCipher in decodeList:
            print("Decode selected")
        else:
            print("Error: Entry must be (e/d)")
            continue
        break

    #asks the user for an entry to encode or decode
    userCipher = input("Enter what you would like to encode/decode: ")
    if len(userCipher) < 1:
        userCipher = "This is a Caesar cipher. It's encrpyted!"
        print("Default entry selected.")

    #asks the user for an amount by which to shift the alphabet for encoding or decoding the user's entry
    while True:
        shiftNum = input('Enter a number by which to shift the cipher along the alphabet (1-25): ')
        if len(shiftNum) < 1:
            shiftNum = 13
            print("Default number selected.")
        try:
            shiftNum = int(shiftNum)
        except:
            print("Error: Entry is not a number.")
            continue
        if 1 <= shiftNum <= 25:
            break
        else:
            print("Error: The number you entered is out of bounds.")
            continue

    #runs the function that encodes or decodes the user's entry
    Encrypter(userCipher)

    #asks the user if they'd like to perform more operations, and lets the program end if they don't
    while True:
        newCipher = input("Would you like to process another cipher? (y/n): ")
        if len(newCipher) < 1:
            newCipher = 'y'
            print("Default selected: y")
        if newCipher not in yesList + noList:
            print("Error: Entry must be (y/n)")
            continue
        break
    if newCipher in yesList:
        continue
    else:
        break
