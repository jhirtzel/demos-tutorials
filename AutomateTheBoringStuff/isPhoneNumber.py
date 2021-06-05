import itertools, re

def isPhoneNumber(text):
    """Assumes American phone number pattern: 123-456-7890
        3 digit area code (optional)
        7 digit phone number
        separated by hyphens

        This sucks without regex
    """
    if len(text) != 12:
        return False
    for i in itertools.chain(range(0,3), range(4,7), range(8,12)):
        if not text[i].isdecimal():
            return False
    if text[3] != '-' or text[7] != '-':
        return False
    # for i in range(4,7):
    #     if not text[i].isdecimal():
    #         return False
    # for i in range(8,12):
    #     if not text[i].isdecimal():
    #         return False
    return True

print('Is 415-555-4242 a phone number?')
print(isPhoneNumber('415-555-4242'))
print('Is Moshi moshi a phone number?')
print(isPhoneNumber('Moshi moshi'))
    