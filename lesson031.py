print(type(1+1))
print(type(2 * 3))
print(type(4 - 10))
print(type(3 ** 6))
print(type(2/3))
print(type(10/2))
print(10/2)
print('-'*80)

import math
print(math.floor(3.15))
print(math.floor(3.999999))
print(math.floor(-3.14))
print(math.floor(-3.0000001))
print(math.floor(-3.0000000000001))
print(math.floor(-3.0000000000000001))
print('-'*80)

a = 33
b = 16
print(a/b)
print(a//b)
print(math.floor(a/b))
print('-'*80)


a = -33
b = 16
print(a/b)
print(a//b)
print(math.floor(a/b))
print(math.trunc(a/b))
print('-'*80)

a = -33
b = 16
print(a/b)
print(a//b)
print(math.floor(a/b))
print(math.trunc(a/b))
print('-'*80)

# a = b*(a//b) + (a%b)
a = 13
b = 4
print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a%b))
print( a == b*(a//b) + (a%b) )
print('-'*80)




