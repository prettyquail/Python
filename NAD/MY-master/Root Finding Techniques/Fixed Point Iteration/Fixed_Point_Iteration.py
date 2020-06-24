

def f(x):
    return (x**3 - 9*x + 1 )


def g(x):
    return (9*x-1)**(1/3)

epsilon = 0.0001


x = 2.7

x_before = 0

i = 0

while (abs(x - x_before) > epsilon):
    x_before = x
    x = g(x)

    print(i, "{0:.6f}".format(x), "{0:.6f}".format(abs(x - x_before)))
    i = i + 1
