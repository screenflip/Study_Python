# coding:shift-jis

n = 11

if n % 15 == 0:
    print("Fizz Buzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)

if n==11:
    print("n is",n)
else:
    print("n",'is','not',11)
    print("n", 'is', n)

if __name__=="__main__":
    print("スクリプト時のみ")
