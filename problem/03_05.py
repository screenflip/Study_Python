#coding:shift-jis

# デフォルト引数が活用されていて良いですね
# 再帰関数でスマートにかけていていいと思います
def fib(n,f0=0,f1=1):
    if n<=1:
        if n==1:
            return f1
        elif n==0:
            return f0
        else:
            return
    else:
        return fib(n-1,f1,f0+f1)

print(fib(10))
