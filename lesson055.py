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

a = []
b = ''
c = ()
d = {}
e = set()
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print()

a = [1, 2]
b = 'abc'
c = (1, 2)
d = {'a':1}
e = set((1,2))
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print('='*80)

print(bool(None))
print()
a = [1,2,3]
if a is not None and len(a) > 0:
    print(a[0])
else:
    print('Nothing to see here...')
print()

if a:
    print(a[0])
else:
    print('Nothing to see here...')
print()

if bool(a):
    print(a[0])
else:
    print('Nothing to see here...')
print()

a = []
if bool(a):
    print(a[0])
else:
    print('Nothing to see here...')
print()

a = None
if a:
    print(a[0])
else:
    print('Nothing to see here...')
print('-'*80)

a = [1, 2]
if len(a) > 0 and a is not None:
    print(a[0])
else:
    print('Nothing to see here...')
print()

a = []
if len(a) > 0 and a is not None:
    print(a[0])
else:
    print('Nothing to see here...')
print()

# a = None
# if len(a) > 0 and a is not None:
#     print(a[0])
# else:
#     print('Nothing to see here...')
# print()

a = None
if a is not None and len(a) > 0:
    print(a[0])
else:
    print('Nothing to see here...')
print()



