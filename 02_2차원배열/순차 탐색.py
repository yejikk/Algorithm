def sequent(a, n, key):
    for i in range(n):
        if a[i] == key:
            return 1
    return -1

data = [4, 9, 11, 23, 2, 19, 7]
key = 3
print(sequent(data, len(data), key))