from itertools import combinations

l, k = map(int, input().split())
ary = sorted(list(input().split()))
vowels = {'a', 'e', 'i', 'o', 'u'}
combs = combinations(ary, l)

for comb in combs:
    hasVowel = any(char in vowels for char in comb)
    consonant_count = sum(1 for char in comb if char not in vowels)
    if hasVowel and consonant_count >= 2:
        print(''.join(map(str, comb)))
