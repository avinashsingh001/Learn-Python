print("Guess the secret no which is between 1 and 25")
guess_count = 1
secret = 16
while guess_count <= 3:
    guess = int(input('Guess :'))
    guess_count = guess_count + 1
    if guess == secret:
        print("you win!")
        break
else:
    print("you failed!")
