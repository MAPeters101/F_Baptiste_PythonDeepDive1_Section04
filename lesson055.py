print(bool(1))
print(bool(0))
print(bool(-1))
print(bool(-100))

help(int)

print(100 != 0)
print(bool(100))
print((100).__bool__())
print()
print(bool(0))
print((0).__bool__())
print('-'*80)

help(list)
a = []
print(bool(a))
print(a.__len__())
print(bool(a.__len__()))
print('-'*80)

print(bool(0.0))
print(bool(0+0j))
print()

from decimal import Decimal
from fractions import Fraction
print(bool(Fraction(0, 1)))
print(bool(Fraction(1, 1)))
print(bool(Decimal('0.0')))
print(bool(Decimal('0.1')))
print()

print(bool(10.5))
print(bool(1j))
print(Fraction(1,2))
print(Decimal('10.5'))
print('-'*80)


