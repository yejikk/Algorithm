def solution(phrases, second):
    if second % 28 == 0:
        output = '_' * 14

    else:
        q = second % 28
        if q < 14:
            output = ('_' * (14-q)) + phrases[:q]
        elif q > 14:
            output = phrases[(q-14):] + ('_' * (q-14))
        else:
            output = phrases

    print(output)

phrases = 'happy-birthday'
second = 20
solution(phrases, second)