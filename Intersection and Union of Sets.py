>>> odds=set([1,3,5,7,9])
>>> evens=set([2,4,6,8,10])
>>> primes=set([2,3,5,7])
>>> composites=set([4,6,8,9,10])
>>> odds.union(evens)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
>>> evens.union(odds)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
>>> odds
{1, 3, 5, 7, 9}
>>> evens
{2, 4, 6, 8, 10}
>>> odds.intersection(primes)
{3, 5, 7}
>>> primes.intersection(evens)
{2}
>>> evens.intersection(odds)
set()
>>> primes.union(composites)
{2, 3, 4, 5, 6, 7, 8, 9, 10}
