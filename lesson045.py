import decimal
from decimal import Decimal

print(decimal.getcontext())
print(decimal.getcontext().rounding)
print(decimal.getcontext().prec)

decimal.getcontext().prec = 6
print(decimal.getcontext())
print(decimal.getcontext().prec)
print('-'*80)

g_ctx = decimal.getcontext()
print(type(g_ctx))
print(g_ctx)
print()

g_ctx.rounding = 'ROUND_HALF_UP'
print(g_ctx)
print(g_ctx.rounding)
print()

g_ctx.rounding = decimal.ROUND_HALF_UP
print(type(decimal.ROUND_HALF_UP))
print(decimal.ROUND_HALF_UP)

print(g_ctx)
print(g_ctx.rounding)
print('-'*80)

g_ctx.prec = 28
g_ctx.rounding = decimal.ROUND_HALF_EVEN
print(decimal.getcontext())
print('-'*80)

print(decimal.localcontext())
print(type(decimal.localcontext()))
print(type(decimal.getcontext()))
print('-'*80)

with decimal.localcontext() as ctx:
    print(type(ctx))
    print(ctx)

    ctx.prec = 6
    ctx.rounding = decimal.ROUND_HALF_UP
    print(ctx)
    print(decimal.getcontext())
    print(decimal.localcontext())
    print(id(ctx) == id(decimal.getcontext()))
    print('-'*80)




