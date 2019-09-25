def solution(n, words):
    answer = []

    person = [0] * (n + 1)

    word = words.pop(0)
    temp = [word]

    i = 1
    dic = {}
    dic[word] = [i]
    person[i] += 1

    flag = 0

    while words:
        i += 1
        seq = i % n
        if not seq:
            seq = n
        person[seq] += 1

        word = words.pop(0)

        if temp[-1][-1] == word[0]:
            if word not in dic:
                dic[word] = [seq]
            else:
                answer = [seq, person[seq]]
                flag = 1
                break

        else:
            answer = [seq, person[seq]]
            flag = 1
            break

        temp.append(word)
    if not flag:
        answer = [0, 0]
    print(answer)
    return answer

solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])