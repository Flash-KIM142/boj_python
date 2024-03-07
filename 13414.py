import sys

input = sys.stdin.readline
k, l = map(int, input().split())
stud_dict = dict()
for i in range(l):
    cur = input().rstrip()
    stud_dict[cur] = i
result = list(sorted(stud_dict.items(), key=lambda x: x[1]))
if k > len(result):
    k = len(result)
for i in range(k):
    print(result[i][0])
