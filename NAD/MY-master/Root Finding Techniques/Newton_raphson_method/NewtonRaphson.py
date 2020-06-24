import math
def func(x):
    return x*x*x-3*x+1

def derivFunc(x):
    return 3*x*x-3

def NewtonRaphson(x):
    h=func(x)/derivFunc(x)
    while(abs(h)>=0.0001):
        h=func(x)/derivFunc(x)
        x=x-h
    print("The value of root is : ","%.4f"%x) 

x=0.3
NewtonRaphson(x)
