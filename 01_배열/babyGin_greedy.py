# num = 456789
# num = input()
num = "012345" # int로 받으면 0을 없애고 12345로 나온다.
c = [0] * 12 # index 체크를 하기 위해서 12까지 돌린다.

for i in range(6):
    c[int(num[i])] += 1

i = 0
tri = 0
run = 0
while i < 10:
    if c[i] >= 3:
        c[i] -= 3
        tri += 1
        continue

    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue

    i += 1

if tri+run == 2 :
    print("babyGin")
else:
    print("Not")
