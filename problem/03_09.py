#coding:shift-jis

# 良いですね
from isper import is_perfect

def my_filter(rang,func):
    for i in rang:
        if func(i):
            print(i)


my_filter(range(1,1000),is_perfect)
