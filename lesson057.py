print(True or True and False)
print(True or (True and False))
print((True or True) and False)
print('-'*80)

a = 10
b = 2
if a/b > 2:
    print('a is at least twice b')

# a = 10
# b = 0
# if a/b > 2:
#     print('a is at least twice b')

a = 10
b = 0
if b > 0 and a/b > 2:
    print('a is at least twice b')

if b > 0:
    if a/b > 2:
        print('a is at least twice b')

if b > 0 and a/b > 2:
    print('a is at least twice b')

if b and a/b > 2:
    print('a is at least twice b')

b = 1
if b and a/b > 2:
    print('a is at least twice b')

b = None
if b and a/b > 2:
    print('a is at least twice b')

# if b > 0 and a/b > 2:
#     print('a is at least twice b')
print('-'*80)

import string
help(string)

a = 'c'
print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.ascii_letters)
print(string.digits)
print('-'*80)

name = 'Bob'
if name[0] in string.digits:
    print("Name cannot start with a digit.")

name = '1Bob'
if name[0] in string.digits:
    print("Name cannot start with a digit.")

# name = ''
# if name[0] in string.digits:
#     print("Name cannot start with a digit.")

name = ''
if len(name) > 0 and name[0] in string.digits:
    print("Name cannot start with a digit.")

name = ''
if len(name) and name[0] in string.digits:
    print("Name cannot start with a digit.")

name = ''
if name and name[0] in string.digits:
    print("Name cannot start with a digit.")
print()

name = 'abc'
print(bool(name))
name = ''
print(bool(name))
print('-'*80)





