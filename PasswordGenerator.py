#
######################################################################
# Password Generator by The Bannon Brothers!!!!
# Requirements:
#   1. Create simple string variables w/ 'A-Z' 'a-z' and '0-9'
#   2. Min pass length: 8 / Max pass length: 26
#
######################################################################

import os     # Imports Operating System

# Character sets for password generator
capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowers = "abcdefghijklmnopqrstuvqxyz"
numbers = "0123456789"
special_chars = "!@#$%^&*()_-=[]{}|;:',<.>/?`~"
#length = 0
all_chars = capitals + lowers + numbers + special_chars
password = ""
t = os.times()
seed = int((t.user + t.system + t.elapsed) * 8675309)
seeds = []

# Ask user how long they want their generated password to be.
length = int(input("How long would you like your password? (Min:8 - Max:26) "))
if length < 8:
    print("Password too short.")
elif length < 27:
    print("Password length accepted!")
else:
    print("Password too long, how the fuck are you supposed to remember that?!")

seed = seed % length

for i in range(length):
    bag_of_seeds = (seed * (i + 2300000) + i * i) ^ (seed * (i % 5))
    number = bag_of_seeds % length
    seeds.append(number)

# x = ord("A") - ord will get the ASCII value of "A"

random_keys = input("Press random keys!!! ")
for i in range(length):
    rk = random_keys[i % len(random_keys)]
    pseudo_random = (ord(rk) + i * seeds[i]) % len(all_chars)
    password += all_chars[pseudo_random]
else:
    print(f"Your random password is: {password}")

