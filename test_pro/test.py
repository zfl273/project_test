num = 1
num1 = 2
num2 = 3

def add_fun(num=0,*args):
    for i in args:
        num += i
    return num

num3 = 4
add_fun(1,2,3,4,5)
