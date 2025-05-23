def product (x,y,z):
    result = x*y*z
    print(f"The product of {x}, {y} and {x} is {result}")

#Return statement ends the function execution and sends the value back.
#Return multiple values
def get_stats(a,b):
    return a+b,a-b


def divisionByTwo(a,b):
    try:
        return a/0,b/0
    except ZeroDivisionError:
        return 0,0
    



def main():
    product (4,5,9)
    sum,subtract = get_stats(20,12)

    print(f"Sum: {sum}")
    print(f"Subtract: {subtract}")


    ans1,ans2 = divisionByTwo(8,4)
    print(f"8/2 = {ans1}")
    print(f"4/2 = {ans2}")

    #lambda function
    add = lambda a,b:a+b
    print(f"The sum of 2 plus 3 is {add(2,3)}")
    square = lambda a:a*a
    nums = [1,2,3,4,5]
    for num in nums:
        print(f"The square of {num} is {square(num)}")

    

    x = 4

    if x % 2 == 0:
        raise Exception("This is an even number")
    else:
        print(f"{x} is an odd number")

    

if __name__ == "__main__":
    main()
    #Assignment2 is to write a program to find the factorial of a number.
    #Write a program to handle errors, the program should  ask for two number using input and then
    #divides them. use an infinite loop to keep asking until a valid input is provide.