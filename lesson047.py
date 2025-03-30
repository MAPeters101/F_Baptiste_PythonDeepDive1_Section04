import decimal
from decimal import Decimal

help(Decimal)

print(Decimal(10))
print(type(Decimal(10)))
print(Decimal(-10))
print(Decimal('10.1'))
print(Decimal('-3.1415'))
print()
t = (0, (3,1,4,1,5), -4)
print(Decimal(t))
print(Decimal((0, (3,1,4,1,5), -4)))
#print(Decimal(0, (3,1,4,1,5), -4))
print(Decimal((1, (3,1,4,1,5), -4)))
print(Decimal((1, (3,1,4,1,5), -3)))
print('-'*80)

print(format(0.1, '.25f'))
print(Decimal(0.1))
print(Decimal('0.1'))
print(Decimal(0.1) == Decimal('0.1'))
print(Decimal(10) == Decimal('10'))
print('-'*80)

