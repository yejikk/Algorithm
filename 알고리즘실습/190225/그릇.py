dish = ')(()()())((('

dishsum = 10
for i in range(1, len(dish)):
    if dish[i-1] != dish[i]:
        dishsum += 10
    else:
        dishsum += 5

print(dishsum)