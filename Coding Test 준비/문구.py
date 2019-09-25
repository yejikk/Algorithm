def solution(phrases, second):
    output = ['_'] * 14
    phrases = list(map(str, phrases))

    for i in range(second):
        v = phrases.pop(0)
        w = output.pop(0)
        output.append(v)
        phrases.append(w)

    print(''.join(output))

phrases = 'happy-birthday'
second = 27
solution(phrases, second)