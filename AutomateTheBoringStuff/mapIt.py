#! python3
# mapIt.py

import webbrowser as browser, sys, pyperclip

if len(sys.argv) > 1:
	#if we had an arg, parse the address from it
	address = ' '.join(sys.argv[1:])
else:
	address = pyperclip.paste()

print ('+'.join(address.trim(',').split()))
