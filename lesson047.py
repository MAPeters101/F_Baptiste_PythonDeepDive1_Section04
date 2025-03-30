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

print(decimal.getcontext())
decimal.getcontext().prec = 6
a = Decimal('0.123456789')
print(a)
print()

decimal.getcontext().prec = 2
a = Decimal('0.12345')
b = Decimal('0.12345')
print(a)
print(b)
print(0.12345 + 0.12345)
print(a + b)






