n = int(input())
robots = dict()
for i in range(n):
    robots[input()] = dict()

n = int(input())
for i in range(n):
    com = input().split()
    method = com[0]
    if method == 'add':
        name = com[1]
        topic = com[2]
        val = int(com[3])
        if topic in robots[name]:
            robots[name][topic] += val
        else:
            robots[name][topic] = val
    elif method == 'say':
        robot1 = com[1]
        robot2 = com[2]
        common = set(robots[robot1].keys()).intersection(robots[robot2].keys())
        if common:
            top = list()
            for i in common:
                common_min = min(robots[robot1][i], robots[robot2][i])
                top.append(f'{i} {common_min}')
            top.sort()
            print(*top, sep=', ')
        else:
            print('Empty')