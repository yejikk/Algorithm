import sys
sys.stdin = open("d3-4.txt")

test = int(input())

for tc in range(1, test+1):
    student, submit = map(int, input().split())
    person = list(map(int, input().split()))

    total = list(range(1, student+1))

    for n in person:
        if n in total:
           total.remove(n)
    total = ' '.join(map(str, total))
    print(f'#{tc} {total}')