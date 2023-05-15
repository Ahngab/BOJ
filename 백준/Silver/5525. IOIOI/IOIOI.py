import sys

N = int(sys.stdin.readline().strip())
length = int(sys.stdin.readline().strip())
sentence = sys.stdin.readline().strip()
count = 0
string = "I" + "OI"*N


for i in range(length -len(string) +1):
    if sentence[i:i+len(string)] == string:
        count += 1
print(count)