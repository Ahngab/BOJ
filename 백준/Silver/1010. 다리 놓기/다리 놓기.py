import math

def cal_bridge(x,y):
    return math.comb(y,x)

n = int(input())
for i in range(n):
    m, n = map(int,input().split())
    print(cal_bridge(m, n))