# import sys
# !{sys.executable} -m pip install bcrypt
import bcrypt

password = b"studyhard"
# Hash a password for the first time, with a certain number of rounds
salt = bcrypt.gensalt(14)
hashed = bcrypt.hashpw(password, salt)
print(salt)
print(hashed)

print( bcrypt.checkpw(password, hashed) )