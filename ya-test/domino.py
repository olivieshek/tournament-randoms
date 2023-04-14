n, m = list(map(int, input().split()))
if not (n * n - m * m) % 2:
    print('YES')
    print((n * n - m * m) // 2)
else:
    print('NO')