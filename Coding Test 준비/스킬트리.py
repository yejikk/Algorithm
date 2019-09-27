def solution(skill, skill_trees):
    answer = 0
    for word in skill_trees:
        flag = 0
        temp = ''
        for i in range(len(word)):
            if word[i] in skill:
                temp += word[i]
        print(temp)
        for i in range(len(temp)):
            if temp[i] != skill[i]:
                flag = 1
                break
        if not flag:
            answer += 1
    return answer

solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])