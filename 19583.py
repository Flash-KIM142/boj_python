import sys


def time_to_min(time) :
    return 60 * time[0] + time[1]


input = sys.stdin.readline
s, e, q = input().split()
s = list(map(int, s.split(':')))
e = list(map(int, e.split(':')))
q = list(map(int, q.split(':')))
s_min = time_to_min(s)
e_min = time_to_min(e)
q_min = time_to_min(q)
answer = 0
entrance_dict = dict()
while True:
    line = input().rstrip()
    if len(line) > 1:
        time, name = line.split()
        time = list(map(int, time.split(':')))
        cur_time_min = time_to_min(time)
        if cur_time_min <= s_min:  # 입장
            entrance_dict[name] = 1
        elif e_min <= cur_time_min <= q_min and name in entrance_dict:
            entrance_dict[name] += 1
    else:
        break
for key in entrance_dict:
    if entrance_dict[key] >= 2:
        answer += 1
print(answer)
