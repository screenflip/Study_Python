# coding:shift-jis

def gcd(a=252, b=105):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd())

print(gcd(1232, 2352))

print(gcd(b=4385, a=2895))

print(gcd(123))

print(gcd(b=123))

def printer(a, b, **args):
    print('a:', a)
    print('b:', b)
    for key in args:
      print('!', key, args[key])

printer(a='apple', b='banana', c='candy', d='donuts', e='Eclair')

def printer2(a, *args):
    print(a)
    print(args)

printer2('apple', 'banana', 'candy', 'donuts')

def add3(x=10):
    return x + 3

print(add3(5))

print(add3)

f = add3

print(f)

print(f(5))
