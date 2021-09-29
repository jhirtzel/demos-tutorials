#! python3
# mcb..pyw - A multi-clipboard program

import sys, pyperclip, shelve

usage = """mcb.pyw - Persistent clipboard storage
    mcb.pyw [save] <keyword>
        saves keyword to the clipboard

    mcb.pyw <keyword>
        loads keyword to the clipboard 

    mcb.pyw [list] 
        loads all keywords to clipboard
"""

if len(sys.argv) != 1:
    print(f'{usage}')
    sys.exit(1)

mcbShelf = shelve.open('mcb')

if len(sys.argv == 3) and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()       # save the keyword if we had 2 arguments
elif len(sys.argv) == 2:
    # list keywords and their content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))  # list all the keys
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])       # if we had a specific key, copy its contents


mcbShelf.close()


