#CHALLENGE 77: Vowel finding with tuples
#GOAL: Write code that has tuple with many random words. Then, prints the vowels present in each word
#SKILL: Learning about tuples

wordsT=('learn', 'teach', 'ball', 'pencil', 
        'eraser', 'doctor', 'engineer', 'python', 
        'software', 'underneath')

vowelsT=('a', 'e', 'i' ,'o', 'u')


for word in wordsT:
    text=''
    for i in range (0, 5):
        for j in range (0, len(word)-1):
            if (word[j]==vowelsT[i]) and (text.find(vowelsT[i])==-1):
                if (len(text)!=0):
                    text+=', '
                text+=vowelsT[i]

    print(f'The word {word.upper()} has the vowels {text}')
