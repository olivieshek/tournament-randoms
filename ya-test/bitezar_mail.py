# import re
t = input()
vowels = 'aeiouy'
# v_letters = re.findall(fr'[{vowels}]', t)
# c_letters = re.findall(fr'[^{vowels}]', t)
v_name = str()
c_name = str()
for l in t:
    if l in vowels:
        v_name += l
    else:
        c_name += l

print(v_name)
print(c_name)

max_name = max(v_name, c_name, key=len)
min_name = min(v_name, c_name, key=len)

for idx, letter in enumerate(max_name):
    diff = list(letter + min_name[idx])
    diff.sort()
    if diff[-1] in v_name:
        print('Vowel')
    else:
        print('Consonant')

