import decimal
from decimal import Decimal

# n = d * (n//d) + (n%d)
x = 10
y = 3
print(x//y, x%y)
print(divmod(x, y))
print( x == 7 * (x//y) + (x%y))
print('-'*80)





