from collections import deque

answer = 0
dq = deque()
n, m = map(int, input().split())
for i in range(1, n + 1):
    dq.append(i)
targets = list(map(int, input().split()))
for target in targets:
    if target == dq[0]:
        dq.popleft()
        continue
    for i in range(len(dq)):
        if dq[i] == target:
            if i > len(dq) // 2:  # 3번 연산 수행
                for _ in range(len(dq) - i):
                    dq.appendleft(dq.pop())
                    answer += 1
            else:  # 2번 연산 수행
                for _ in range(i):
                    dq.append(dq.popleft())
                    answer += 1
            break
    dq.popleft()
print(answer)
