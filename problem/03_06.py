#coding:shift-jis

def my_sum(*args):
#   sum も組み込み関数になっているので使わないようにしてください
#   関数名がmy_sumなのはそういう理由です（笑）
    sum=0
    for i in args:
        sum+=i
    return sum
