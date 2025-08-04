#CHALLENGE 65: Data analisys
#GOAL: Write code that takes in as many integers as the user wants and then print out the highest, the lowest and the average
#SKILL: Learning about while loops

lst=[]
lst.append( int(input('Type in an integer: ')) )
greatest= lst[0] 
lowest= lst[0] 
sum = lst[0] 
i=1

flag= ( (input('Do you wish to type in another number? (Y/N): ')).strip()).upper()
while(flag not in 'nN'):
    if flag not in 'Yy':
        print('That is not a valid option!')

    else:
        lst.append( int(input('Type in an integer: ')) )
        sum+=lst[i]

        if(lst[i]<lowest):
            lowest=lst[i]

        if(lst[i]>greatest):
            greatest=lst[i]

        i+=1
    flag= ( (input('Do you wish to type in another number? (Y/N): ')).strip()).upper()

print(f'Before stopping, the mean of the numbers you typed in were {(sum/i):.2f}')
print(f'The greatest number you typed was {greatest}')
print(f'The lowest number you typed was {lowest}')