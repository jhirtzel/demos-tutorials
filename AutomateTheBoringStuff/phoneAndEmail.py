#! python3
# phoneAndEmail.py - finds phone numbers and emails on the clipboard

import pyperclip, re, pprint

#create phone number regex
phoneRegex = re.compile(r"""(
    (\d{3}|\(\d{3}\))?  #area code group: optional 3 digits, with or without parentheses
    (\s|-|\.)?          #optional separator
    (\d{3})             #first 3 digits
    (\s|-|\.)?          #another optional separator
    (\d{4})             #last 4 digits
    (\s*[ex|x|ext.]\s*(\d{2,5}))?                  #optional extension
    )""",re.VERBOSE)

#create email regex
#TODO capture "+identifier" part of username as separate group
emailRegex = re.compile(r"""(
    ([a-zA-Z0-9._%+-]+)           #username part
    @
    ([a-zA-Z0-9.-]+)              #domain
    (\.[a-zA-Z]{2,4})             #top level domain suffix (.com, .gov, .uk, etc)
    )""",re.VERBOSE)

#TODO find matches on clipboard
text = str(pyperclip.paste())
matches = []

print('Phone groups:')
for groups in phoneRegex.findall(text):
    pprint.pprint(groups)
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[6] != '':
        phoneNum = phoneNum + 'x' + groups[6]
    matches.append(phoneNum)

print('Email groups:')
for groups in emailRegex.findall(text):
    pprint.pprint(groups)
    matches.append(groups[0])

#TODO copy results back to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or emails found on clipboard.')