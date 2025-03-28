from fractions import Fraction
help(Fraction)

print(Fraction(1))
print(Fraction(1, 1))
print(Fraction(denominator=1, numerator=2))
print()
print(Fraction(2,1))
print(Fraction(1,2))
print(Fraction(numerator=1, denominator=2))
print(Fraction(0.125))
print(Fraction('0.125'))
print(Fraction('22/7'))
print('-'*80)

x = Fraction(2,3)
y = Fraction(3,4)
print(x+y)
print(x*y)
print(x/y)
print('-'*80)

print(Fraction(8/16))
print(Fraction(1, -4))
print(Fraction(-1, 4))
x = Fraction(1, -4)
print(x.numerator)
print(x.denominator)
print('-'*80)

import math
x = Fraction(math.pi)
print(x)
print(float(x))

y = Fraction(math.sqrt(2))
print(y)
print(float(y))
print('-'*80)

a = 0.125
print(a)
b = 0.3
print(b)
print(Fraction(a))
print(Fraction(b))
print()
print(format(b, '0.5f'))
print(format(b, '0.15f'))
print(format(b, '0.25f'))
print(Fraction(b))
print()

x = Fraction(0.3)
print(x.limit_denominator(10))
print()

x = Fraction(math.pi)
print(x)
print(float(x))
print('-'*80)

print(x.limit_denominator(10))
print(Fraction(22, 7))
print(x.limit_denominator(100))
print(x.limit_denominator(10000))
print(x.limit_denominator(100000))
print(312689/99532)

