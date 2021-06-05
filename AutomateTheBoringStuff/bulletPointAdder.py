#! python3
# bulletPointAdder.py - Adds wiki markdown bullets to each newline item in the clipboard

import pyperclip
TEXT = pyperclip.paste()

lines = TEXT.split('\n')
for i in range(len(lines)):
    lines[i] = '* '+lines[i]
TEXT = '\n'.join(lines)

#print('print\n'+TEXT+'\nendprint')
pyperclip.copy(TEXT)
