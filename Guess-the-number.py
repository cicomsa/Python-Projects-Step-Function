class Error(Exception):
   """Base class for other exceptions"""
   pass

class ValueTooSmallError(Error):
   """Raised when the input value is too small"""
   pass

class ValueTooLargeError(Error):
   """Raised when the input value is too large"""
   pass


import random            
number = random.randrange(1, 11)
guess = int(input("Guess my number between 1 and 10: "))
guesses = 1

while number != guess:
    try:
        guesses += 1
        if guess < number:
            raise ValueTooSmallError
        elif guess > number:
            raise ValueTooLargeError 
    except ValueTooSmallError:
        print("This value is too small, try again!")
    except ValueTooLargeError:
        print("This value is too large, try again!")
    guess = int(input("Guess my number between 1 and 10: "))
print("\n\nGreat, you got it in", guesses,  "guesses!")