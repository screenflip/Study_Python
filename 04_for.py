# coding:shift-jis

s=0
for i in range(1,11):
print(s)
for i in range(0, 50):
  print(i)
  if i >= 10:
    break

for i in range(0, 10):
  if i % 2 == 0:
    continue
  print(i)

import math

n = 101

for i in range(2, int(math.sqrt(n) + 1)):
    if n % i == 0:
        print(n, "は素数ではありません")
        break
else:
    print(n, "は素数です")

for i in range(10):
  print(i)

for i in range(5,10):
  print(i)


for i in range(1,10,2):
  print(i)

for i in range(10, 0, -1):
  print(i)
  if i<5:
      break

print(i)
