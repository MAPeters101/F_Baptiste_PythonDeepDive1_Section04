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

x = 2
x_dec = Decimal(2)

root_float = math.sqrt(x)
root_mixed = math.sqrt(x_dec)
root_dec = x_dec.sqrt()
print(format(root_float, '1.27f'))
print(format(root_mixed, '1.27f'))
print(root_dec)
print()

print(format(root_float * root_float, '1.27f'))
print(format(root_mixed * root_mixed, '1.27f'))
print(root_dec * root_dec)
print('-'*80)


x = 0.01
x_dec = Decimal('0.01')
print(format(x, '.27f'))
print(x_dec)
print()

root_float = math.sqrt(x)
root_mixed = math.sqrt(x_dec)
root_dec = x_dec.sqrt()
print(format(root_float, '1.27f'))
print(format(root_mixed, '1.27f'))
print(root_dec)
print()

print(format(root_float * root_float, '1.27f'))
print(format(root_mixed * root_mixed, '1.27f'))
print(root_dec * root_dec)
print('-'*80)


