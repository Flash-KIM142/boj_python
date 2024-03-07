import sys

input = sys.stdin.readline
n, m = map(int, input().split())
pocketmon_dict = dict()
pocketmon_list = ['Dummy', ]
for i in range(1, n + 1):
    pocketmon = input().rstrip()
    pocketmon_dict[pocketmon] = i
    pocketmon_list.append(pocketmon)
for _ in range(m):
    cmd = input().rstrip()
    if cmd.isdigit():
        print(pocketmon_list[int(cmd)])
    else:
        print(pocketmon_dict[cmd])
