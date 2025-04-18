from decimal import Decimal
import sys
a = 3.14
b = Decimal('3.1415')
print(sys.getsizeof(a))
print(sys.getsizeof(b))
print('-'*80)

import time

def run_float(n):
    for i in range(n):
        a = 3.1415

def run_decimal(n):
    for i in range(n):
        a = Decimal('3.1415')

n = 10_000_000
start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ', end-start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('float: ', end-start)
print('='*80)

def run_float(n):
    a = 3.1415
    for i in range(n):
        a + a

def run_decimal(n):
    a = Decimal('3.1415')
    for i in range(n):
        a + a

n = 10_000_000
start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ', end-start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('float: ', end-start)
print('.'*80)

def run_float(n):
    a = 3.1415
    for i in range(n):
        a * a

def run_decimal(n):
    a = Decimal('3.1415')
    for i in range(n):
        a * a

n = 10_000_000
start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ', end-start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('float: ', end-start)
print('.'*80)

def run_float(n):
    a = 3.1415
    for i in range(n):
        a / a

def run_decimal(n):
    a = Decimal('3.1415')
    for i in range(n):
        a / a

n = 10_000_000
start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ', end-start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('float: ', end-start)
print('-'*80)

import math
n = 5_000_000
def run_float(n):
    a = 3.1415
    for i in range(n):
        math.sqrt(a)

def run_decimal(n):
    a = Decimal('3.1415')
    for i in range(n):
        a.sqrt()

n = 10_000_000
start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ', end-start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('float: ', end-start)
print('-'*80)





