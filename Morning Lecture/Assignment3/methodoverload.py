#Python doesn't support tranditional overloading since it's an interpreted language.
#The last definition of the function is the one that is ran.
#inorder to support it we use external libraries which are installed using pip.
#Note you have to install multipledispatch
from multipledispatch import dispatch
@dispatch(int,int,int)
def sum(a,b,c):
    result = a+b+c
    print(f"(The sum of {a}, {b} and {c} is {result})")
@dispatch(int,int)
def sum(x,y):
    result = x+y
    print(f"(The sum of {x} and {y} is {result})")
    
def main():
    sum(1,2,3)
    sum(2,3)
    
if __name__ == "__main__":
    main()