#CHALLENGE 53: Palindromes
#GOAL: Write code that prints out if the sentence the user provided was a palindrome, regardless of spacing
#SKILL: Learning about for loops

s1 = (input('Type in any sentence: ') ).lower()
s2 = ''
k = 0
total=0

s1Spaceless= s1.replace(' ', '')

for i in range (0, len(s1Spaceless), 1):
    s2 += s1Spaceless[i]

for l in range (0, len(s2)-1, 1):
    if (s1Spaceless[l] == s2[l]):
        total+=1

if(total == len(s2)-1):
    print(f'The sentence "{s1}" is a palindrome (disregarding spacing)!')

else:
    print(f'The sentence "{s1}" is not a palindrome (disregarding spacing)!')