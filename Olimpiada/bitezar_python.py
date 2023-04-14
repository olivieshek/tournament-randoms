L, C, B = list(map(int, input().split()))
text = '''print("Hello,World")'''
print('YES' if len(text) == sum((L, C)) - B else 'NO')