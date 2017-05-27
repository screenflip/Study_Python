# coding:shift-jis

str = input().strip()

while str!="q":
    if str=="":
        str=input().strip()
        continue
    print(str,end="デース\n")
    str=input().strip()
