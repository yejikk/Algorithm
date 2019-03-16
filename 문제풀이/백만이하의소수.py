N = 1000000
number = [0] * (N+1)

for i in range(2, N+1):
    if number[i] == 0:
        for j in range(i*2, N+1, i):
            if number[j] == 1:
                continue
            else:
                number[j] = 1

for k in range(2, N+1):
    if number[k] == 0:
        print(k, end=' ')

