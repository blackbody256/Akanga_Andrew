#Write a program to handle errors, the program should  ask for two number using input and then
#divides them. use an infinite loop to keep asking until a valid input is provide.

def division(a,b):

    if b==0:
        raise ZeroDivisionError
    else:
        return a/b


def main():

    while True:
        a = int(input("Enter the dividend\n:"))
        b = int(input("Enter the divisor\n:"))

        try:
            print(f"The quotient of {a} and {b} is {division(a,b)}")
            break
        except ZeroDivisionError:
            print("The divisor can't be a zero\nTry again\n\n")
        
if __name__ == "__main__":
    main()