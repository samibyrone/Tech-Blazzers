import re

def validate_email(email):

    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    email = input("Please enter your email: ")

    if re.match(regex, email): print("This email address is valid.")

    else: print("Invalid email address. Please include an '@' sign.")
