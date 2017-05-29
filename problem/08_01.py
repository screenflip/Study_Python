#coding:shift-jis

def is_perfect(n):
    sum=0
    for i in range(1,n+1):
        if n%i==0:
            sum+=i
    if sum==2*n or n==0:
        return True
    else:
        return False

if __name__=="__main__":
    n_max=200
    for n in range(1,n_max+1):
        print(n,":",is_perfect(n),end="\t")
        if n%5==0:
            print()
