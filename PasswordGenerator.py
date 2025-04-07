#
######################################################################
# Password Generator by The Bannon Brothers!!!!
# Requirements:
#   1. Create simple string variables w/ 'A-Z' 'a-z' and '0-9'
#   2. Min pass length: 8 / Max pass length: 26
#
######################################################################

# Character sets for password generator
capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowers = "abcdefghijklmnopqrstuvqxyz"
numbers = "0123456789"
#length = 0
all_chars = capitals + lowers + numbers
password = ""

# Ask user how long they want their generated password to be.
length = int(input("How long would you like your password? (Min:8 - Max:26) "))
if length < 8:
    print("Password too short.")
elif length < 26:
    print("Password length accepted!")
else:
    print("Password too long, how the fuck are you supposed to remember that?!")

# x = ord("A")
# print(x)
for i in range(length):
    pseudo_random = (ord(input("Press random keys!!! ")[0]) + i * 17) % len(all_chars)
    password += all_chars[pseudo_random]
    print(password)