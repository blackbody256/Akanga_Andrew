#the external library is called multipledispatch

from multipledispatch import dispatch
@dispatch(int,int,int)
def sum(a,b,c):
    result = a+b+c
    print(result)
@dispatch(int,int)
def sum(x,y):
    result = x+y
    print(result)
    
sum(1,2,3)
sum(2,3)