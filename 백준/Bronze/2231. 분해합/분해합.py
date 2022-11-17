number = int(input())
temp = 1
while True:
    if number == temp + sum(list(map(int, list(str(temp)) ))):
        print(temp)
        break
    elif number == temp:
        print(0)
        break
    else:
        temp += 1