#coding:shift-jis

is_perfect=__import__('03_08').is_perfect

def my_filter(rang,func):
    for i in rang:
        if func(i):
            print(i)


my_filter(range(1,1000),is_perfect)
