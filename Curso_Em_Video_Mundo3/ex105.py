#CHALLENGE 105: Student grade analysis
#GOAL: Write code that takes in many student grades and creates a dictionary with the highest, the lowest,
#the average, and (optionally) a report of the class grades
#SKILL: Learning about functions pt2

def classAnalysis(grades: list, report= False):
    """
    The function classAnalysis() is meant to read a list of student grades and then find the
    highest, the lowest, the average and a literal report
    param grades: list of student grades in float
    param report: bool that measures if the user wants the report
    return: dictionary with many informations
    """
    dic= dict()
    dic['Average']= sum(grades)/len(grades)
    dic['Highest']= max(grades)
    dic['Lowest']=min(grades)

    if report:
        match dic['Average']:
            case a if a<3:
                dic['Report']='Really bad'

            case a if 3<=a<5:
                dic['Report']='Bad'

            case a if 5<=a<7:
                dic['Report']='Regular'

            case a if 7<=a<9:
                dic['Report']='Good'

            case a if 9<=a:
                dic['Report']='Really good'

    avg= f'{dic['Average']:.2f}'
    dic['Average']= float(avg)

    return dic

l=[]

while True:
    flag= ( (input('Would you like to add another number to your list? (Y/N): ')).strip()).upper()
    if(flag=='N'):
        rep= input('Would you like to a report of the student average? (Press anything for yes): ')
        break
    elif(flag!='Y'):
        print('That is not a valid option!', end=' ') 
        continue

    num= float(input(f'Type in a grade: '))

    while(num<0):
        print('That is not a valid option!', end=' ') 
        num= float(input(f'Type in a grade: '))

    l.append(num)
    print('Number added successfully!')

print(classAnalysis(l, rep))
#print(help(classAnalysis))