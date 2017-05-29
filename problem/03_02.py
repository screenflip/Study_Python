#coding:shift-jis

s = input().strip()

while s!="q":
#   空文字をチェックしてるのはナイス
#   ちなみに，空文字はFalseの判定になるので if str: ともかけます
    if s:
        print(s,end="デース\n")
    s=input().strip()
# 凸守かカレンか…
# str は文字列にキャストするための組み込み関数があるので使わないほうがよさそうです
# Python では，組み込み関数ですら上書きできてしまうので注意が必要です
# 組み込み関数一覧はこちら https://docs.python.jp/3/library/functions.html
# < 気を付けます
