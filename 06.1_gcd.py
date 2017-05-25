
def gcd2(a=252, b=105):
    if b == 0:
        print("answer is",a)
        return a
    else:
        print("--",a,"%",b,"=",a%b)
        return gcd2(b, a % b)

def p_gcd2(a,b):
    print(gcd2(a,b))

p_gcd2(123.3,246.6)
