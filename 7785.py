import sys

input = sys.stdin.readline
n = int(input())
people = dict()
for _ in range(n):
    name, status = input().split()
    if status == 'enter':
        people[name] = 1
    else:
        people[name] = 0

result = []
for key in people.keys():
    if people[key] == 1:
        result.append(key)
result.sort()
result.reverse()
for name in result:
    print(name)
