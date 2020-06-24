import math

def l1(y,z):
    return 0.1*(3+(5*y)+(2*z) )


def l2(x,z):
    return 0.1*(3+(4*x)+(3*z))

def l3(x,y):
    return 0.1*(-3-x-(6*y))

epsilon=0.001
x=l1(0,0)
y=l2(0,0)
z=l3(0,0)
x=l1(y,z)
y=l2(x,z)
z=l3(x,y)
n=int(input("Enter the number of iterations"))
i=0
for i in range(n):
    x=l1(y,z)
    y=l2(x,z)
    z=l3(x,y)
   
    i = i + 1
print("x=")
print(round(x,3))
print("y=")
print(round(y,3))
print("z=")
print(round(z,3))

