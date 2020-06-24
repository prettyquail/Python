
  
   
import math
def f(x): 
    return x*x - x -1
   

def RegularFalsy(a,b): 
  
    if (f(a) * f(b) >= 0.0): 
        print("Invalid Interval\n") 
        return
   
    m=(a*f(b)-b*f(a))/(f(b)-f(a))
    while (abs(f(m))>= 0.01): 
  
        
        m=(a*f(b)-b*f(a))/(f(b)-f(a))
        if(f(m)==0.0):
            break

        if (f(m)*f(a) < 0.0): 
            b = m
        else: 
            a = m
              
    print("The value of root is : ","%.4f"%m) 
      

a =1.0
b = 2.0
RegularFalsy(a, b) 
  
