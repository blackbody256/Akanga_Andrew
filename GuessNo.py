import random

def main():
    secret_num = random.randint(1,10)
    guess = int(input("Guess the number:\t"))
    attempt = 0
    while True:
        if guess == secret_num:
            attempt += 1
            print (f"You are correct the secret number is {guess}")
            print(f"it took you {attempt} times to guess")
            break
        elif guess < secret_num:
            attempt+=1
            guess = int(input("Too low try again:\t"))
        else:
            attempt +=1
            guess = int(input("Too high try again:\t"))

if __name__ == "__main__":
    main()

