import random
import string
from random import sample, choice
#Define
aantal = input("How many? \n")
filename = "users_gen.txt"
chars = "qwertyuiopasdfghjklzxcvbnm1234567890"
#Clear file
open(filename, 'w').close()
#Open file
file = open(filename, 'a')
#Loop
for x in range(int(aantal)):
	username = ''.join(choice(chars) for _ in range(10))
	password = ''.join(choice(chars) for _ in range(5))
	file.write(username + ":" + password + "\n")
#Close
file.close()