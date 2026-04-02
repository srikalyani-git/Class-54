def func1(n):
    print(n*(n+1)/2)

func1(4)


def func2(n):
    sum=0
    for i in range(1,n+1):
        sum +=i
    return sum

print(func2(4))

def func3(n):
    sum=0
    for i in range(1,n+1):
        for j in range(1,i+1):
            sum+=1
    print(sum)

func3(4)
