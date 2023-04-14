n = int(input())
prod = 1
for i in range(n):
    prod = (int(input()[-1]) * prod) % 10

print(prod)

# res = 1
# for i in a:
#     res = int(str(res * i)[-1])


# for i in range(n):
# 	int(input()[-1]) * 

# print(res)

# # 3 45 67 89 ==> 5
