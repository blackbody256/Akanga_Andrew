def factorial(num):
    if num < 0:
        raise Exception("There is no factorial of a negative.")
    elif num > 1:
        return num * factorial(num-1)
    else:
        return 1
    

def main():
    num = int(input("Enter a number to get it's factorial:\n"))
    print(f"The factorial of {num} is {factorial(num)}")

if __name__ == "__main__":
    main()