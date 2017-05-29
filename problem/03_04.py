#coding:shift-jis

def Goldbach(max_n=101, printer=print):

    if max_n<=4:
        return True

    printer(4,2,2)

    if max_n<=6:
        return True

    p_list=[]

    for n in range(3,max_n,2):
        flag=True
        for p in p_list:
            if n%p==0:
                flag=False
                break
            elif n<p**2:
#               p_list.append(n) をここでしたら，フラグを立てなくてすみそう
                break
        if flag==True:
            p_list.append(n)

    f=True

    for n in range(6,max_n,2):
        flag=False
        for m in p_list:
            M=n-m
            if M in p_list:
                printer(n,m,M)
                flag=True
                break
            elif m>M:
#               printer(n, '-', '-')
#               f=False
#               return False とやれば，フラグが全部いらなくなりそう
                break
        if not flag:
            printer(n,'-','-')
            f=False
#   return True
    return f

# フラグを使うと，読みにくいコードができることが多いので，フラグを立てなくて済む方法がないか少し考える癖をつけるといいかもしれないです

if __name__=="__main__":
    Goldbach()
