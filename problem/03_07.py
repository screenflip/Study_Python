#coding:shift-jis

def add_n(n):
    def add_n_(a):
        return a+n
    return add_n_

print(add_n(1)(5))

f=add_n(119)

g=add_n(99)

print(f(1))

print(g(1))

print(add_n(add_n(f(add_n(12)(18)))(g(2)))(f(1)))
