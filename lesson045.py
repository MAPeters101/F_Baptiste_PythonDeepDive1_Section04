import decimal
from decimal import Decimal

print(decimal.getcontext())
print(decimal.getcontext().rounding)
print(decimal.getcontext().prec)

decimal.getcontext().prec = 6
print(decimal.getcontext())
print(decimal.getcontext().prec)
print('-'*80)


