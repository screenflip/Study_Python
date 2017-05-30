#coding:shift-jis

def Goldbach(max_n=101, printer=print):

    if max_n<=4:
        return True

    printer(4,2,2)

    if max_n<=6:
        return True

#       <最初にp_listに2を入れておけば、効率が落ちることもなく4を特別扱いする必要もないのでは？
#       <あと、else も消せますし
#   p_list=[2]
    p_list=[]

    for n in range(3,max_n,2):
        for p in p_list:
            if n%p==0:
                break
            elif n<p**2:
                p_list.append(n)
                break
#       p_listが最初は空で、ずっと空のままになるのでelseを付けました
        else:
            p_list.append(n)

    f=True

    for n in range(6,max_n,2):
        for m in p_list:
            M=n-m
            if M in p_list:
                printer(n,m,M)
                break
            elif m>M:
                printer(n, '-', '-')
                f=False
#               ここでは、例外が見つかっても最後まで続けるようにしたかったので、fは残します
                break
    return f

if __name__=="__main__":
    Goldbach()
