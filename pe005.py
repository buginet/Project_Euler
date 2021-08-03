from math import gcd
from functools import reduce
print(reduce(lambda x, y: int(x*y/gcd(x,y)), range(1, 21)))
