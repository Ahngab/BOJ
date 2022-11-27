from collections import deque

while True:
    sentence = input()
    flag = True

    if sentence == ".":
        break
    else:
        stack = deque([])

        for i in sentence:
            if ( i == "(" ) or ( i == "[" ):
                stack.append(i)

            elif ( i == "]" ):
                if ( len(stack) != 0 ) and ( stack[-1] == "[" ):
                    stack.pop()
                else:
                    stack.append("]")
                    break
            
            elif ( i == ")" ):
                if ( len(stack) != 0 ) and ( stack[-1] == "(" ):
                    stack.pop()
                else:
                    stack.append(")")
                    break
        
        
        print("yes") if len(stack) == 0 else print("no")