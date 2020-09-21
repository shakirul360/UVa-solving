def paranthesis_balance(string):
    stack = []
    openings = [ "(", "[" ]
    for char in string:
        if char in openings:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == "(":
                if char != ")":
                    return False
            if current_char == "[":
                if char != "]":
                    return False
    
    if stack:
        return False
    else:
        return True

n = int(input())
for i in range(n):
    string = input()
    if paranthesis_balance(string) == True:
        print("Yes")
    else:
        print("No")
