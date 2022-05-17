#########################################################
# Code to generate the random password in pythons
# first import the important modules
import random
import string

print("Hello, welcome to the password generator.")

# Ask for the length of the password 
len=int(input("Enter the required length for the password."))

# define data
lower=string.ascii_lowercase
upper=string.ascii_uppercase
num=string.digits
symbols=string.punctuation

# Random combination
all=lower+upper+num+symbols

# create random string
temp=random.sample(all,len)

# Generate password
password="".join(temp)

# print password
print("YOUR PASSWORD IS \n"+password)

########################################################################