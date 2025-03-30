import decimal
from decimal import Decimal

# n = d * (n//d) + (n%d)
x = 10
y = 3
print(x//y, x%y)
print(divmod(x, y))
print( x == 7 * (x//y) + (x%y))
print('-'*80)

x = Decimal(10)
y = Decimal(3)
print(x//y, x%y)
print(divmod(x, y))
print( x == 7 * (x//y) + (x%y))
print()

x = -10
y = 3
print(x//y, x%y)
print(divmod(x, y))
print( x == 7 * (x//y) + (x%y))
print()

x = Decimal(-10)
y = Decimal(3)
print(x//y, x%y)
print(divmod(x, y))
print( x == 7 * (x//y) + (x%y))
print('-'*80)

help(Decimal)

a = Decimal('0.1')
print(a.ln())
print(a.exp())
print(a.sqrt())

import math
#print(math.ln(a))
print()
print(math.exp(a))
print(math.sqrt(a))
print('-'*80)





