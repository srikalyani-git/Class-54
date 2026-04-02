def func1(m,n):
    print(m*n)

def func2(m,n):
    res = 0
    for i in range (1,n+1):
        res += m
    print(res)

func1(10,20)
func2(10,20)