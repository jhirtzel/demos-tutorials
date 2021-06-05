#! python3
# mclip.py - A multi-clipboard program

TEXT = {
    'agree': """Yes, I agree. That sounds fine to me.""",
    'busy': """Sorry, I have a conflict. Can we reschedule?""",
    'upsell': """Would you consider upgrading to a monthly donation?"""
}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copies the text for keyphrase')
    sys.exit()
keyphrase = sys.argv[1]         #get the first command line arg as the key

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f"Text for {keyphrase} copied to clipboard")
else:
    print(f"No text found for {keyphrase}")