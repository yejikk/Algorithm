import sys
sys.stdin = open('스파이조직.txt')

N, spy = map(str, input().split())
N = int(N)

result = []
secret = []
for name in spy:
    if name == '>':
        if result[-1] == '<':
            result.pop()
        else:
            while result[-1] != '<':
                result.pop()
            result.pop()
    else:
        if name != '<':
            if result:
                if result[-1] != '<':
                    p = result.pop()
                    result.append(p+name)
                else:
                    result.append(name)
            else:
                result.append(name)
        elif name == '<':
            if len(result) == (2 * N) + 1:
                if result[-1] not in secret:
                    secret.append(result[-1])
            result.append(name)

for i in secret:
    print(i, end=' ')