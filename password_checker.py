# importing the built-in regular expression module to aid in search patterns e.g. upper, lowercase, numbers, symbols, etc...

import re

# adding a function to take user input to check length is at least 8 characters.

def check_password_strength(password):
  score = 0
  
  if len(password) >= 8: # checking the length of the password to ensure it is 8 characters or above.
    score += 1
  else:
    print("Password must be at least 8 characters long.")
  
  if re.search(r"[A-Z]", password): # Checking the password has an uppercase character.
    score += 1
  else: 
    print("Password must contain at least 1 uppercase character.")
  
  if re.search(r"[a-z]", password): # Checking the password has a lowercase character.
    score += 1
  else:
    print("Password must contain at least 1 lowercase character.")
  
  if re.search(r"/d", password): # Checking the password has a number.
    score += 1
  else:
    print("Password must contain at least 1 number.")
  
  if re.search(r"[!@#$^%&*(),.?\":{}<>]", password): # Checking the password has a special character.
    score += 1
  else:
    print("Password must contain at least 1 special character !@#$^%&*(),.?\":{}<>")
  
  return score

password = input("Enter a password to check: ")
print("Password strength:", check_password_strength(password), "/5")
