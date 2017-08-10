from banner import *

def main(file):
	print "hi"
	#source https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files
	try:
		f = open(file)
	except Exception:
		raise ZeroDivisionError