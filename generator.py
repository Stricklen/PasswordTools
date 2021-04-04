from random import randint, choice


def genPass(leng,sym,num,upp,low):
    # Initialises blank password
    my_passwrd = ""
    if [sym,num,upp,low] == [0,0,0,0]:
        return my_passwrd
    else:
        # Iterates until generated password is long enough
        while len(my_passwrd) < int(leng):
            # Randomly picks the new type of new char
            j = randint(0,3)
            # Check if picked char is symbol and if symbols are enabled
            if j == 0 and sym == 1:
                # Random symbol ascii value chosen 
                r = randint(*choice([(33, 47), (58, 64), (91, 96), (123,126)]))
                # Ascii converted into char
                new = chr(r)
                # New char added to my_passwrd
                my_passwrd += new
            # If number and if enabled
            elif j == 1 and num == 1:
                new = chr(randint(48,57))
                my_passwrd += new
            # If uppercase and enabled
            elif j == 2 and upp == 1:
                new = chr(randint(65,90))
                my_passwrd += new
            # if lowercase and enabled
            elif j == 3 and low == 1:
                new = chr(randint(97,122))
                my_passwrd += new
        return my_passwrd
    print("ERROR: Password failed to generate")

def strengthTest():
    return

if __name__ == '__main__':
    print(genPass("11",0,0,0,0))

# Ascii:
# ord(n) finds the ascii number for a char
# chr(n) finds the ascii char for a number

# 65-90 is A-Z (uppercase)
# 97-122 is a-z (lowercase)
# 48-57 are  0-9 (numbers)

# 33-47 are: !"#$%&'()*+,-./
# 58-64 are: :;<=>?@
# 91-96 are: [\]^_`
# 123-126 are: {|}~
# (symbols)
