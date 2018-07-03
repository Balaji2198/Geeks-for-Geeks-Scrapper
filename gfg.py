#!/usr/bin/python3

from bs4 import BeautifulSoup
import os, sys
import requests

BASE_URL = 'https://www.geeksforgeeks.org/'
WARNING_COLOR = '\033[93m'
END_COLOR = '\033[0m'
FAIL_COLOR = '\033[91m'

def line_break(Number):
	line = '=' * Number
	print ('\033[96m' + line + '\033[0m')

def displayContent(URL):
	req 	= requests.get(URL)
	soup	= BeautifulSoup(req.text, 'lxml')
	pres	= soup.find_all('pre')
	no_code	= True

	for pre in pres:
		if "brush" in str(pre):
			no_code	= False
			print (pre.text)
			line_break(80)
	if no_code:
		print (WARNING_COLOR + 'Enter a link with code!' + END_COLOR)

def main():
	if len(sys.argv) == 2:
		if BASE_URL in sys.argv[1]:
			displayContent(sys.argv[1])
		else:
			print (WARNING_COLOR + "I've been programmed to work only for " + BASE_URL  + END_COLOR)
	else:
		print (WARNING_COLOR + 'Invalid Command' + END_COLOR)


if __name__ == '__main__':
	main()
