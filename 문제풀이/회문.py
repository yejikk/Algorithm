import sys
sys.stdin = open("회문.txt")

def palindrome(word):
    result = list(word)
    for i in range(len(result)//2):
        x = result[i]
        result[i] = result[len(result)-1-i]
        result[len(result)-1-i] = x
    return ''.join(result)

test = int(input())

for tc in range(1, test+1):
    word = input()
    result = palindrome(word)
    if word == result:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')