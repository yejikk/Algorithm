# 문자열 비교 == (eq) 하나하나씩 비교해서 실행

def strcmp(str1, str2):
    i = 0 # index를 위한 변수
    if len(str1) != len(str2): # str1과 str2의 len이 다르면 이미 다른 문자열
        return False # 다른 문자열이기 때문에 False

    else: # 길이가 같다면 하나하나씩 비교해서 같은 문자열인지 비교한다.
        while i < len(str1):
            if str1[i] != str2[i]: # 다르면 return False
                return False
            i += 1
    return True

a = "abc"
b = "abb"
print(strcmp(a, b))
print(a == b)