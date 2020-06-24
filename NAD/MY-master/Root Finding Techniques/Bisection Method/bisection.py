
  
   
import math
def f(x): 
    return x*x - x -1
   

def bisection(a,b): 
  
    if (f(a) * f(b) >= 0.0): 
        print("Invalid Interval\n") 
        return
   
    m=(a+b)/2
    while (abs(f(m))>= 0.01): 
  
        
        m= (a+b)/2
        if(f(m)==0.0):
            break

        if (f(m)*f(a) < 0.0): 
            b = m
        else: 
            a = m
              
    print("The value of root is : ","%.4f"%m) 
      

a =1.0
b = 2.0
bisection(a, b) 
  
