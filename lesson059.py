
print('a' or [1,2])
print('' or [1,2])
print(1 or 1/0)
#print(0 or 1/0)
print('-'*80)

s1 = None
s2 = ''
s3 = 'abc'

s1 = s1 or 'n/a'
s2 = s2 or 'n/a'
s3 = s3 or 'n/a'
print(s1)
print(s2)
print(s3)
print([] or [0])
print(None or [0])
print('-'*80)

print(None and 100)
print([] and [0])
print()


a = 2
b = 4
if b == 0:
    print(0)
else:
    print(a/b)

a = 2
b = 0
if b == 0:
    print(0)
else:
    print(a/b)
print()

a = 2
b = 4
print(a/b)

a = 2
b = 0
print(b and a/b)
print('-'*80)

s1 = None
s2 = ''
s3 = 'abc'
#print(s1[0])
#print(s2[0])
print(s3[0])
print()

print(s1 and s1[0])
print(s2 and s2[0])
print(s3 and s3[0])
print()

print((s1 and s1[0]) or '')
print((s2 and s2[0]) or '')
print((s3 and s3[0]) or '')
print('-'*80)

print((s1 and s1[0]) or 'n/a')
print((s2 and s2[0]) or 'n/a')
print((s3 and s3[0]) or 'n/a')
print('='*80)




