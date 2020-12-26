import sys
sys.stdout = open('2.SimpleArraySum/output.txt','w')
sys.stdin = open('2.SimpleArraySum/input.txt','r')


def simpleArraySum(ar):
    i = 0
    for x in ar:
        i += x
    return i

num1 = int(input())
ar = list(map(int, input().rstrip().split()))
res = simpleArraySum(ar)
print(res)
