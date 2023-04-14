n = input()
m = input()
a = 10
mass = [0] * a
res = 0
for i in range(a):
    mass[i] = [False] * a

for i in range(len(max(n, m, key=len))):
    mass[int(n[i])][int(m[i])] = True
    mass[int(m[i])][int(n[i])] = True

# print(*mass, sep='\n')
for el in mass:
    res += el.count(True)

print(res)