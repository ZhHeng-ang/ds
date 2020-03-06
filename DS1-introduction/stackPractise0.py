'''
使用'除二'算法，将输入的十进制数字转换成八位二进制
'''

from pythonds.basic.stack import Stack

def divide2(desNumber):
    s = Stack()

    while desNumber > 0:
        rem = desNumber % 2
        s.push(rem)
        desNumber = desNumber//2

    binSting = ""
    while not s.isEmpty():
        binSting = binSting + str(s.pop())
    return binSting
print(divide2(233))    















