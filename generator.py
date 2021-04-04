from random import randint, choice

def findAscii(string):
    string_ascii = []
    for letter in string:
        string_ascii += str(ord(letter))

## TESTING SYMBOL SELECTION
# my_passwrd = ""
# for i in range(20):
#     r = randint(*choice([(33, 47), (58, 64), (91, 96), (123,126)]))
#     new = chr(r)
#     my_passwrd += new
# print(my_passwrd)


def genPass(leng,sym,num,upp,low):
    # Initialises blank password
    my_passwrd = ""
    # Iterates until generated password is long enough
    while len(my_passwrd) < int(leng):
        # Randomly picks the new type of new char
        j = randint(0,3)
        # Check if picked char is symbol and if symbols are enabled
        if j == 0 and sym == True:
            # Random symbol ascii value chosen 
            r = randint(*choice([(33, 47), (58, 64), (91, 96), (123,126)]))
            # Ascii converted into char
            new = chr(r)
            # New char added to my_passwrd
            my_passwrd += new
        # If number and if enabled
        elif j == 1 and num == True:
            new = chr(randint(48,59))
            my_passwrd += new
        # If uppercase and enabled
        elif j == 2 and upp == True:
            new = chr(randint(65,90))
            my_passwrd += new
        # if lowercase and enabled
        elif j == 3 and low == True:
            new = chr(randint(97,122))
            my_passwrd += new
    return my_passwrd

# Ascii:
# ord(n) finds the ascii number for a char
# chr(n) finds the ascii char for a number

# 65-90 is A-Z (uppercase)
# 97-122 is a-z (lowercase)
# 48-59 are  0-9 (numbers)

# 33-47 are: !"#$%&'()*+,-./
# 58-64 are: :;<=>?@
# 91-96 are: [\]^_`
# 123-126 are: {|}~
# (symbols)

# findAscii("hello")


# string = "hello"
# blank = ""
# for c in string:
#     ord(c)