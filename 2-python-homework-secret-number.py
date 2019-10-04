secret = 8

guess = int(input("Guess the number.. it is somewhere between 1 and 10: "))

if guess == secret:
    print("You are correct! The secret number is 8.")

else:
    print("Nope! You got the wrong number! Try again!")