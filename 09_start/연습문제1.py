bit = '0000000111100000011000000111100110000110000111100111100111111001100111'

for i in range(0, len(bit), 7):
    binary = bit[i:i+7]
    n = 0
    for j in range(len(binary)):
        n = n * 2 + int(binary[j])
    print(n)