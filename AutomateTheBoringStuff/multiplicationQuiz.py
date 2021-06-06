import pyinputplus as pyip, random, time

numberOfQuestions = 3
correctAnswers = 0

for question in range(numberOfQuestions):
    #pick a couple of random numbers
    num1 = random.randint(1,12)
    num2 = random.randint(2,13)

    prompt = 'Q# %s: %s x %s\n' % (question+1,num1,num2)

    try:
        #correct answers are handled by allowRegex
        #incorrect answers are handled by blockRegex, with a custom message
        #this works because "allow" takes precedence over "block"

        pyip.inputStr(prompt,
                allowRegexes=['^%s$' % (num1 * num2)], #calculate the product and sub into the regex
                blockRegexes=[('.*','Incorrect!')],       #return Incorrect! to any other input
                timeout=8,
                limit=3
        )

    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct!')
        correctAnswers += 1
        time.sleep(1)  #pause to read the output

print('Final score: %s / %s' % (correctAnswers, numberOfQuestions))