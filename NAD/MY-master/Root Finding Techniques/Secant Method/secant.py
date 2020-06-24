
  
   
import math
def f(x): 
    return x*x*x - x -1
   

def secant(a,b): 
  
    if (f(a) * f(b) <0.0):
        while True:
            m=(a*f(b)-b*f(a))/(f(b)-f(a))
            a=b
            b=m

            if (abs(f(m)) < 0.0001):
                break 
        print("Root",round(m,4))
    else:
        print("Cannot find roots")

a =1.0
b = 2.0
secant(a, b) 
  
