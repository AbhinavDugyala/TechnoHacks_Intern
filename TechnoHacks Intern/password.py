import random as r
import string as s
result=s.ascii_letters+s.digits+s.punctuation
length=int(input("Enter length of your password:"))
for x in range(length):
    print (r.choice(result),end="")