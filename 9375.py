t = int(input())
for _ in range(t):
    n = int(input())
    clothes = dict()
    for _ in range(n):
        item_name, item_type = input().split()
        if item_type not in clothes:
            clothes[item_type] = 1
        else:
            clothes[item_type] += 1
    tmp = 1
    for key in clothes:
        tmp *= (clothes[key] + 1)
    print(tmp - 1)
