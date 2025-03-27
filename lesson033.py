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
print()

def encode(digits, digit_map):
    if max(digits) >= len(digit_map):
        raise ValueError("digit_map is not long enough to encode the digits")
    # encoding = ''
    # for d in digits:
    #     encoding += digit_map[d]
    # return encoding
    return ''.join([digit_map[d] for d in digits])

print(encode([15, 15], '0123456789ABCDEF'))
print('-'*80)

def rebase_from10(number, base):
    digit_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if base < 2 or base > 36:
        raise ValueError('Invalid base: 2 <= base <= 36')
    sign = -1 if number < 0 else 1
    number *= sign

    digits = from_base10(number, base)
    encoding = encode(digits, digit_map)
    if sign == -1:
        encoding = '-' + encoding
    return encoding




