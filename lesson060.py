print(0.1 is (3+4j))
print(3 is 3)
print([1,2] is [1,2])
print()

print('a' in 'this is a test')
print(3 in [1,2,3])
print(3 not in [1,2,3])
print('-'*80)

print('key1' in {'key1' : 1})
print(1 in {'key1' : 1})
print('-'*80)

print(3 < 5)
#print(1 + 1j < 3 + 4j)

from decimal import Decimal
from fractions import Fraction
print(4 < Decimal('10.5'))
print(Fraction(2,3) < Decimal('0.5'))
print('-'*80)

print(4 == 4 + 0j)
print(True == Fraction(2,2))
print(True < Fraction(3,2))
print('='*80)

print(1 < 2 < 3)
print(1 < 2 and 2 < 3)
print()
print(3 < 2 < 1/0)
print(3 < 2 and 2 < 1/0)
#print(3 < 4 < 1/0)
#print(3 < 4 and 2 < 1/0)
print('-'*80)