# 使用函数，求前n个整数的和
def sumOFN(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum+1
    return sum
print(sumOFN(10))


# 高斯函数
def sumOFN2(n):
    return (n(n+1))/2