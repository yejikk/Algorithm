import sys
sys.stdin = open('스파이조직.txt')

N, spy = map(str, input().split())
print(spy)

secret = []
num = ''
for name in spy:
    if name != '<' and name != '>':
        num += name
    else:
        if num != '':
            secret.append(num)
            num = ''
        secret.append(name)
print(secret)