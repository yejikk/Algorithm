# 정수를 문자열 정수로 나타내기

def itoa(num):
    result = []
    while num != 0:
        r = num % 10
        result.append(chr(r + ord('0')))
        num //= 10

    result.reverse()
    result = ''.join(result)
    return result

num = 123
print(num, type(num))
str1 = itoa(num)
print(itoa(num), type(str1))