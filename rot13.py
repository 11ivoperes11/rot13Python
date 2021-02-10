# receives character and converts to rot13 character
def rotFunc(i):
    char = i
    asciiConvert = ord(char)    # convert charachter into ascii code
    # if ascii number greater than 110, subrtact 13 from ascii code
    if asciiConvert >= 110: # >=110 is charachters from n onwards
        asciiConvert = asciiConvert - 13
        rot13Convert = chr(asciiConvert)
    elif asciiConvert >= 65 and asciiConvert <= 77: # capital A to M chars
        rot13Convert = chr(asciiConvert + 13)
    elif asciiConvert >= 78 and asciiConvert <= 90: # capital N to Z chars
        asciiConvert = asciiConvert - 13
        rot13Convert = chr(asciiConvert)
    # else add 13 charachters to ascii code
    else:    
        rot13Convert = chr(asciiConvert + 13) # all other chars
    # return output to function
    return rot13Convert

# welcome message 
print ("Welcome to the rot13 program, here your input strings will be encrypted in rot13")
# get user string
rawString = input("Please enter a word to be encrypted: ")
print ("Thank you, you've typed: " + rawString)
rawString = rawString.replace(" ", "")  # ignore spaces
print("Your whitespaces have been removed: " + rawString)
print ("Your rot13 encrypted text:")
# for loop goes through each character of the string
# sends each charater to Rot13 conversion function
for i in range(0, len(rawString)):
    rawChar = rawString[i]  # fetch each character
    rot13Char = rotFunc(rawChar)    # send character to rot13 function
    print (rot13Char, end='')   # print return of rot13 function
print("\n")