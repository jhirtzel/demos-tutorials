#! python3
# errorExample.py

import logging
import traceback

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

def spam():
	bacon()

def bacon():
	raise Exception('This is an error message')

try:
	bacon()
except:
	errorFile = open('errorExample.log','w')
	errorFile.write(traceback.format_exc())
	errorFile.close()
	print('Error information written to errorExample.log')

