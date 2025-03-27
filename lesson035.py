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





