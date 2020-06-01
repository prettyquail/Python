"""List vs Tuples
Lists                  |     Tuples
Add data               |  Cannot be changed
Remove data            |  "Immutable"
Take larger size       |  Takes less space to store
Take more time         |  Made quickly
"""

import sys

list_eg=[1,2,3,"a","b","c",True,3.14159]
tuple_eg=(1,2,3,"a","b","c",True,3.14159)

print("List size=",sys.getssizeof(list_eg))
print("tuple size=",sys.getsizeof(tuple_eg))

import timeit
list_test=timeit.timeit(stmt="[1,2,3,4,5]",number=1000000)
tuple_test=timeit.timeit(stmt="(1,2,3,4,5)",number=1000000)

print("List time:",list_test)
print("Tuple time:",tuple_test)

