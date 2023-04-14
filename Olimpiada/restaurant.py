m = int(input())
species = list(map(int, input().split()))
n = int(input())
clients = [0] * n
for i in range(n):
    clients[i] = list(map(int, input().split()))

print(clients)