import random
MAX_VALUE = 100
MIN_VALUE = 1
secret = random.randint(MIN_VALUE, MAX_VALUE)

tries = 0
while True:
    guess = int(input("guess? "))
    tries += 1
    if guess == secret:
        print("Winner")
    elif guess < secret:
        print("Guess higher")
    else:
        print("Guess lower")