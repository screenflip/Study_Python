# coding:shift-jis

s=0
for i in range(1,11): # 1~10まで繰り返す．11までではないので注意
    s += i*i
print(s)
for i in range(0, 50):
  print(i)
  if i >= 10:
    break
#=>0 1 2 3 4 5 6 7 8 9

for i in range(0, 10):
  if i % 2 == 0:
    continue
  print(i)
#=>1 3 5 7 9

import math

n = 101

for i in range(2, int(math.sqrt(n) + 1)):
    if n % i == 0:
        print(n, "は素数ではありません")
        break
else:
    print(n, "は素数です")
# else は for の中で break しなかった場合に実行される
# for の中身が1度も実行されなくても実行されるので注意
#for i in range(10):
#  print(i)
#=>0 1 2 3 4 5 6 7 8 9

#for i in range(5,10):
#  print(i)
#=>5 6 7 8 9

#for i in range(1,10,2):
#  print(i)
#=>1 3 5 7 9
#増加量を決められる

for i in range(10, 0, -1):
  print(i)
  if i<5:
      break
#=>10 9 8 7 6 5 4 3 2 1
#負の増加量も扱える

print(i)
