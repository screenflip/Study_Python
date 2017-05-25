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
# インデントに注意
# インデントの前には:を書く
# else if の代わりに elif が使う

if n==11:
    print("n is",n)
else:
    print("n",'is','not',11)
    print("n", 'is', n)

if __name__=="__main__":
    print("スクリプト時のみ")
