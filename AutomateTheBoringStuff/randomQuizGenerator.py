#! python3
#randomQuizGenerator.py - creates random quizzes, with questions and answers in random order
# along with the answer key

import random, shutil
from pathlib import Path

numOfQuizzes = 35

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery',
'Alaska': 'Juneau',
'Arizona': 'Phoenix',
'Arkansas': 'Little Rock',
'California': 'Sacramento',
'Colorado': 'Denver',
'Connecticut': 'Hartford',
'Delaware': 'Dover',
'Florida': 'Tallahassee',
'Georgia': 'Atlanta',
'Hawaii': 'Honolulu',
'Idaho': 'Boise',
'Illinois': 'Springfield',
'Indiana': 'Indianapolis',
'Iowa': 'Des Moines',
'Kansas': 'Topeka',
'Kentucky': 'Frankfort',
'Louisiana': 'Baton Rouge',
'Maine': 'Augusta',
'Maryland': 'Annapolis',
'Massachusetts': 'Boston',
'Michigan': 'Lansing',
'Minnesota': 'Saint Paul',
'Mississippi': 'Jackson',
'Missouri': 'Jefferson City',
'Montana': 'Helena',
'Nebraska': 'Lincoln',
'Nevada': 'Carson City',
'New Hampshire': 'Concord',
'New Jersey': 'Trenton',
'New Mexico': 'Santa Fe',
'New York': 'Albany',
'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck',
'Ohio': 'Columbus',
'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem',
'Pennsylvania': 'Harrisburg',
'Rhode Island': 'Providence',
'South Carolina': 'Columbia',
'South Dakota': 'Pierre',
'Tennessee': 'Nashville',
'Texas': 'Austin',
'Utah': 'Salt Lake City',
'Vermont': 'Montpelier',
'Virginia': 'Richmond',
'Washington': 'Olympia',
'West Virginia': 'Charleston',
'Wisconsin': 'Madison',
'Wyoming': 'Cheyenne'}

quizHeader = 'Name:\nDate:\nPeriod:\n'


quizFolder = Path.cwd() / 'quizzes'
# clean up or setup the quiz folder
if quizFolder.exists() and quizFolder.is_dir():
    print('Cleaning up resources...')
    try:
        shutil.rmtree('quizzes') #rmtree gets rid of the dir and files, like 'rm -r'
    except OSError as e:
        print ("Error: %s - %s." % (e.filename, e.strerror))
else:
    print('Setting up resources...')
Path.mkdir(quizFolder)

# Generate 35 quiz files.
for quizNum in range(numOfQuizzes):
    quizFile = open(f'{quizFolder}/capitalsQuiz{quizNum + 1}.txt','w')
    answerKeyFile = open(f'{quizFolder}/capitalsQuiz{quizNum + 1}_answers.txt','w')

    quizFile.write(f'{quizHeader}')
    quizFile.write((' '*12) + f'State Capitals Quiz (Form {quizNum + 1})')
    quizFile.write('\n\n')

    #shuffle the questions
    states = list(capitals.keys())
    random.shuffle(states)

    #Loop through all 50 states, making a question for each.
    for questionNum in range(50):
        #create right and wrong answers for this quiz
        correctAnswer = capitals[states[questionNum]]  #states @ this question is the value of the capital
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        #grab 3 wrong answers from the list
        wrongAnswers = random.sample(wrongAnswers,3)    

        answers = [correctAnswer] + wrongAnswers #correct answer must be a list to append it
        # answers = wrongAnswers.append(correctAnswer)
        random.shuffle(answers)

        # write the question and answer to this quiz
        quizFile.write(f'{questionNum+1}) What is the state capital of {states[questionNum]}?\n')
        for i in range(4):
            # write the four possible choices preceded by the letter
            quizFile.write(f'\t{"ABCD"[i]}. {answers[i]}\n')
        quizFile.write('\n')

        # write the answer key
        answerKeyFile.write(f'{questionNum+1}: {"ABCD"[answers.index(correctAnswer)]}\n')

    quizFile.close()
    answerKeyFile.close()
