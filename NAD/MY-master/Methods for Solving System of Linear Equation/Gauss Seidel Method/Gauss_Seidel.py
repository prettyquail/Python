import math

def l1(y,z):
    return (1/83)*(95-(11*y)+(4*z))


def l2(x,z):
    return (1/52)*(104-(7*x)-(13*z))

def l3(x,y):
    return (1/29)*(71-(3*x)-(8*y))


x=l1(0,0)
y=l2(x,0)
z=l3(x,y)

n=int(input("Enter the number of iterations"))
i=1
for i in range(n):
    x=l1(y,z)
    y=l2(x,z)
    z=l3(x,y)
    print("x=")
    print(round(x,3))
    print("y=")
    print(round(y,3))
    print("z=")
    print(round(z,3))
    i = i + 1


