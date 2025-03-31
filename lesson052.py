
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



