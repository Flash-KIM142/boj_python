n = int(input())
egg_ary = [list(map(int, input().split())) for _ in range(n)]
answer = 0
cnt = 0


def backtracking(idx):
    global answer
    global cnt
    if idx == n:
        answer = max(answer, cnt)
        return

    if egg_ary[idx][0] <= 0 or cnt == n - 1:
        backtracking(idx + 1)
        return

    cur_weight = egg_ary[idx][1]
    for i in range(n):
        if i == idx:
            continue
        if egg_ary[i][0] <= 0:
            continue

        # 현재 계란으로 i 계란 친 결과로 update
        target_weight = egg_ary[i][1]
        egg_ary[idx][0] -= target_weight
        egg_ary[i][0] -= cur_weight
        if egg_ary[idx][0] <= 0:
            cnt += 1
        if egg_ary[i][0] <= 0:
            cnt += 1
        # 다음 단계로 넘어가기
        backtracking(idx + 1)
        # 상태 복구
        if egg_ary[idx][0] <= 0:
            cnt -= 1
        if egg_ary[i][0] <= 0:
            cnt -= 1
        egg_ary[idx][0] += target_weight
        egg_ary[i][0] += cur_weight


backtracking(0)
print(answer)
