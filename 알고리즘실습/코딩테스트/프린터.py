def solution(priorities, location):
    answer = 0
    doc = list(map(int, range(len(priorities))))
    num = priorities
    req = doc[location]
    result = []
    cnt = 0

    bk = 0
    while True:
        flag = 0
        n = doc[0]
        for i in range(1, len(doc)):
            if num[i] > num[n]:
                flag = 1
                result.append(doc[i])

                no = doc.pop(0)
                doc.append(no)

                pr = num.pop(0)
                num.append(pr)

                cnt += 1
                if doc[i] == req:
                    bk = 1
                    answer = cnt
                break

        if bk:
            break

        if not flag:
            result.append(n)
            cnt += 1
            if n == req:
                answer = cnt
                break

    return answer

priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))