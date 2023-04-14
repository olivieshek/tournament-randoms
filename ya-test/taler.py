n = int(input())
ex_rates = list(map(int, input().split()))
print(max(ex_rates) - min(ex_rates))