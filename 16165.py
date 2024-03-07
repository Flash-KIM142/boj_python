n, m = map(int, input().split())
team_dict = dict()
personnel_dict = dict()
for _ in range(n):
    team_name = input()
    team_dict[team_name] = []
    team_size = int(input())
    for _ in range(team_size):
        personnel = input()
        team_dict[team_name].append(personnel)
        personnel_dict[personnel] = team_name
for _ in range(m):
    name = input()
    quiz_type = int(input())
    if quiz_type == 0:  # 팀이 주어지고, 소속 가수들의 이름을 출력
        team_dict[name].sort()
        for i in team_dict[name]:
            print(i)
    else:  # 사람이 주어지고, 소속 팀의 이름을 출력
        print(personnel_dict[name])
