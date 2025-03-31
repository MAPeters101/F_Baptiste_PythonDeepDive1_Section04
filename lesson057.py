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

print('-'*80)





