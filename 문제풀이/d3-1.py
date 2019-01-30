import sys
sys.stdin = open("d3-1.txt")

test = int(input())

for tc in range(1, test+1):
    word = input()
    vowel = ['a', 'e', 'i', 'o', 'u']
    result = ''
    for char in word:
        if char not in vowel:
            result += char
    print(f'#{tc} {result}')