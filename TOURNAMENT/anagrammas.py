# n = int(input())
# nums = list()
# for i in range(n):
#     nums.append(int(input()))

# q = int(input())
# questions = list()
# for i in range(q):
#     questions.append(list(map(int, input().split())))


n = 5
nums = [
    123,
    321,
    14,
    113,
    213
]
q = 4
questions = [
    [0, 4, 123],
    [1, 4, 231],
    [2, 3, 312],
    [0, 0, 312]
]


print(i for i in range(questions[0][0], questions[0][1]))
for i in range(questions[0][0], questions[0][1] + 1):
    print(i)