#coding:shift-jis

def add_n(n):
    def add_n_(a):
        return a+n
    return add_n_

print(add_n(1)(5))

f=add_n(123)

g=add_n(98053)

print(f(1))

print(g(1))
