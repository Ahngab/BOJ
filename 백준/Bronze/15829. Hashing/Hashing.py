import sys

data = list(map(lambda x: ord(x) - 96, list(sys.stdin.readlines()[1].strip())))
for i in range(len(data)):
    data[i] =  data[i]*(31**i)
print(sum(data) % 1234567891)