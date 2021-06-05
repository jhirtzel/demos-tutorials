# pigLatin.py - translate a string into Pig Latin

def isVowel(letter):
    vowels = ['a','e','i','o','u','y']
    if letter in vowels:
        return True
    else:
        return False

print("Enter the message to translate to Pig Latin:")
message = input()
translation = [] #list of translated words

for word in message.split():
    #get rid of any non-letter characters in the each word
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    #if that was all the characters, add it & move to next word
    if len(word) == 0:
        translation.append(prefixNonLetters)
        continue

    #then get rid of any non-letter characters at the end
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]

    #save capital/case letter, and make lowercase
    wasUpper = word.isupper()
    # print(wasUpper)
    wasTitle = word.istitle()
    # print(wasTitle)
    word = word.lower()

    #separate initial consonants
    prefixConsonants = ''
    while len(word) > 0 and not isVowel(word[0]):
        prefixConsonants += word[0]
        word = word[1:]

    #append pig Latin ending
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    # reset back to original casing
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    #reassemble the word
    translation.append(prefixNonLetters+word+suffixNonLetters)
print(' '.join(translation))