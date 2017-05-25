# coding:shift-jis

def gcd(a=252, b=105):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd())
# デフォルト引数が使える

print(gcd(1232, 2352))
# 通常の呼び出し

print(gcd(b=4385, a=2895))
# 呼び出しのときに，引数名を指定できる(この場合意味はないが．)
# キーワード引数という

print(gcd(123))
# 指定されてない引数を与えるとエラーになる

print(gcd(b=123))
# 指定されてない引数を与えるとエラーになる

def printer(a, b, **args):
    print('a:', a)
    print('b:', b)
    for key in args:
      print('!', key, args[key])

printer(a='apple', b='banana', c='candy', d='donuts', e='Eclair')
# キーワード引数で余分に与えられたものを，dictionary型(そのうち扱う)で回収することができる

def printer2(a, *args):
    print(a)
    print(args)

printer2('apple', 'banana', 'candy', 'donuts')
# これも，余分に与えられた引数を回収できるが，呼び出しのときにキーワード引数の形で渡されなあったものに対して使う
# これによって可変長の引数を受け取れる(例：print())
def add3(x=10):
    return x + 3

print(add3(5))

print(add3)

f = add3

print(f)

print(f(5))

print(gcd(134.75,2))
