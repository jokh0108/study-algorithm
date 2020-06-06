n = int(input())
league = {}

def update_league(league, team, win1, win2):
    if team not in league:
        league[team] = [1 if win1 > win2 else 0, win1 - win2]
    else:
        league[team][0] += 1 if win1 > win2 else 0
        league[team][1] += win1 - win2

for _ in range(n*(n-1)):
    team1, win1, team2, win2 = input().split()
    win1, win2 = int(win1), int(win2)
    update_league(league, team1, win1, win2)
    update_league(league, team2, win2, win1)

result = sorted([(team, win, profit) for team, (win, profit) in league.items()],
                key=lambda x: (-x[1], -x[2], x[0]))

for team, win, profit in result:
    print(f'{team} {win} {profit}')
