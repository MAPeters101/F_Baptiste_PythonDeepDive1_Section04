print(type(10))
help(int)
a = int()
print(a)
print(int(10.5))
print(int(10.99999))
print(int(True))
print(int(False))
import fractions
a = fractions.Fraction(22, 7)
print(a)
print(float(a))
print(int(a))
print('-'*80)

print(int("12345"))
print(int("101", 2))
print(int("FF", 16))
print(int("ff", 16))
print(int("A", 11))
#print(int("B", 11))
print('-'*80)

print(bin(10))
print(bin(5))
print(oct(10))
print(hex(255))

a = int('101', 2)
print(a)
b = 0b101
print(b)
print('-'*80)

def from_base10(n, b):
    if b < 2:
        raise ValueError('Base b must be >= 2')
    if n < 0:
        raise ValueError('Number n must be >= 0')
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        # m, n = n%b, n//b
        # m = n % b
        # n = n // b
        n, m = divmod(n, b)
        digits.insert(0, m)
    return digits

print(from_base10(10,2))
print(from_base10(255,16))


