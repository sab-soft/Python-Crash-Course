# A program to store three input, calculate average and print 
# congratulation if the average is greater 95

'''
print("Please enter the students score: ")
student1 = int(input('First student: '))
student2 = int(input('Second student: '))
student3 = int(input('third student: '))

totalscore = student1 + student2 + student3

average = totalscore/3

print('Your average is :', average)

if (average >= 95):
    print('Congratulation you did exceedingly well!')
else:
    print('You can do better next time')
'''

# A program to accept student score and print grade 

'''
score = int(input('Please enter your score: '))

if (score>75) & (score<=100):
    print('Youre grade is A')

elif (score > 70) & (score <=74):
    print('Your grade is AB')

elif (score > 65) & (score <= 69):
    print('Your grade is B')

elif (score > 60) & (score <= 64):
    print('Your grade is BC')

elif (score > 55) & (score <= 59):
    print('Your grade is C')

elif (score > 50) & (score <= 54):
    print('Your grade is CD')

elif (score > 45) & (score <= 59): 
    print('Your grade is D')

elif (score > 40) & (score <= 44):
    print('Your grade is E')

elif (score > 0) & (score <= 39):
    print('Your grade is FFF')

else: 
    print('your score is out of range')
'''

# A Program to calculate average and print student's score 

'''
names = ['John', 'Annis', 'Fatimah', 'Caleb', 'Aruna']

maths_score = [67, 88, 78, 75, 60]

english_score = [98, 80, 85, 89, 93]



maths_total = maths_score[0] + maths_score[1] + maths_score[2] + maths_score[3] + maths_score[4]
maths_average = maths_total/len(maths_score)

english_total = english_score[0] + english_score[1] + english_score[2] + english_score[3] + english_score[4]
english_average = english_total/len(english_score)

print('Average score of stduents in Maths is: ', maths_average)
print('Average score of students in English is: ', english_average)


number = len(names)
    
for index in list(range(number)):
    n = names[index]

    total = maths_score[index] + english_score[index]

    print('Names' '\t\t' 'Total Score' )

    print(n, '\t\t', total)
            
'''