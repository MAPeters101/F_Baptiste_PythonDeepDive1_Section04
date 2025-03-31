
help(complex)

a = complex(1,2)
b = 1 + 2j
c = 1 + 2j
print(a == b)
print(a == c)
print(a.real)
print(type(a.real))
print(a.imag)
print(type(a.imag))
print(a.conjugate())
print('-'*80)

a = 1 + 2j
b = 10 + 8j
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a ** 2)
print(a ** b)
#print(a//b)
#print(a%b)
#print(divmod(a, b))
print('-'*80)

a = 0.1j
print(format(a.imag, '.25f'))
print(a + a + a == 0.3j)
print(format((a + a + a).imag, '.25f'))
print(format((0.3j).imag, '.25f'))
print('-'*80)

import math
print(math.sqrt(2))
print(math.pi)

import cmath
print(cmath.pi)
print(type(cmath.pi))
a = 1 + 2j
#print(math.sqrt(a))
print(cmath.sqrt(a))
print('-'*80)

a = 1 + 1j
print(cmath.phase(a))
print(cmath.pi/4)
print(abs(a))
print(cmath.rect(math.sqrt(2), math.pi/4))
print('='*80)

RHS = cmath.exp(cmath.pi * 1j) + 1
print(RHS)
print(cmath.isclose(RHS, 0))
print(cmath.isclose(RHS, 0, abs_tol=0.0001))


print()
RHS = cmath.exp(complex(0, math.pi)) + 1
print(RHS)
print(cmath.isclose(RHS, 0))
print(cmath.isclose(RHS, 0, abs_tol=0.0001))


