string = '2+3*4/5'
result = ''
stack = []

for char in string:
    if char.isdecimal():
        result += char
    else:
        stack.append(char)

for i in range(len(stack)):
    n = stack.pop()
    result += n

print(result)