import sys
import string


def text_analyzer(string=None):
	"""
	? This function is supposed to take a single string argument
	? and displays the total number of printable characters,
	? and respectively : the number of upper-case
	? characters, lower-case characters, punctuation characters and spaces.

	?	example of usage :

	? text_analyzer("Python 2.0, released 2000, introduced
	? features like List comprehensions and a garbage collection
	? system capable of collecting reference cycles.")
	? The text contains 143 printable character(s):

	?	expected output:
	? The text contains 143 printable character(s):
	? -	2 upper letter(s)
	? -	113 lower letter(s)
	? -	4 punctuation mark(s)
	? - 18 space(s)
	"""
	index = 0
	upper_number = 0
	is_lower = 0
	punctuation = 0
	printables = 0;
	is_space = 0
	if (string is None):
		print("provid a string please!")
		return
	elif (not isinstance(string, str)):
		print("AssertionError: argument is not a string")
		return

	for char in string:
		if (char.isprintable()):
			printables += 1;
		if (char.isupper()):
			upper_number += 1
		elif(char.islower()):
			is_lower += 1
		elif(char.isprintable()) and not (char.isspace()) and not (char.isalnum()):
			punctuation += 1
		elif(char.isspace()):
			is_space += 1
		index += 1

	print(f"The text contains {printables} printable character(s):")
	print(f"- {upper_number} upper letter(s)")
	print(f"- {is_lower} lower letter(s)")
	print(f"- {punctuation} punctuation mark(s)")
	print(f"- {is_space} space(s)")

if __name__ == "__main__":
	if	len(sys.argv) == 2:
		text_analyzer(sys.argv[1])
	else:
		text_analyzer()