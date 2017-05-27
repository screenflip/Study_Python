#coding:shift-jis

for n in range(1,101):
    if n%15==0:
        print("Fizz Bazz")
    elif n%3==0:
        print("Fizz")
    elif n%5==0:
        print("Bazz")
    else:
        print(n)
