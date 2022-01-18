import random
import string

all = string.ascii_letters
_passwords = ""
_file = open("test.txt", "w")
for i in range(100):
    password = "".join(random.sample(all,25))
    _passwords += password + "\n"
    
print(_passwords)
_file.write(_passwords)
_file.close()