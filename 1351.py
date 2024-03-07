from collections import defaultdict

a = defaultdict(int)
a[0] = 1
a[1] = 2
n, p, q = map(int, input().split())


def is_num_exists(num):
    if a[num] != 0:
        return a[num]
    a[num] = is_num_exists(num // p) + is_num_exists(num // q)
    return a[num]


print(is_num_exists(n))
