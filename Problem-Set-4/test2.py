import string

def load_words(file_name):
	'''
	file_name (string): the name of the file containing
	the list of words to load

	Returns: a list of valid words. Words are strings of lowercase letters.

	Depending on the size of the word list, this function may
	take a while to finish.
	'''
	print("Loading word list from file...")
	# inFile: file
	inFile = open(file_name, 'r')
	# wordlist: list of strings
	wordlist = []
	for line in inFile:
		wordlist.extend([word.lower() for word in line.split(' ')])
	print("  ", len(wordlist), "words loaded.")
	return wordlist


def is_word(word_list, word):
	'''
	Determines if word is a valid word, ignoring
	capitalization and punctuation

	word_list (list): list of words in the dictionary.
	word (string): a possible word.

	Returns: True if word is in word_list, False otherwise

	Example:
	>>> is_word(word_list, 'bat') returns
	True
	>>> is_word(word_list, 'asdf') returns
	False
	'''
	word = word.lower()
	word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
	return word in word_list

WORDLIST_FILENAME = 'words.txt'


# Creating an dictionary with each letter matched to a number from 0 to 52.
origial_dict = dict(zip(string.ascii_uppercase + string.ascii_lowercase, range(0,52)))

list_dict = list(2*(string.ascii_uppercase + string.ascii_lowercase))

lower_alphabet = list(string.ascii_lowercase)
upper_alphabet = list(string.ascii_uppercase)

shift_dict = origial_dict

shift = 1

word_list = ['hello', 'yes']

def creating_shift_dict(shift):
	for k, v in origial_dict.items():
		if k in lower_alphabet:
			new_value = v + shift
			shift_dict[k] = new_value
		elif k in upper_alphabet:
			new_value = v + shift
			shift_dict[k] = new_value
	return(shift_dict)


def shifting_dict():
	for k, v in shift_dict.items():
		shift_dict[k] = list_dict[v]
	return(shift_dict)





def cipher_text(text, shift):
	shift_dict = creating_shift_dict(shift)
	shift_dict = shifting_dict()
	list_text = list(text)
	cipher_word = []
	for letter in list_text:
		if letter == ' ':
			cipher_word.append(' ')
		else:
			letter = shift_dict[letter]
			cipher_word.append(letter)
	cipher_word = ''.join(cipher_word)
	return(cipher_word)



#print(cipher_text('hello',1))

# decoding a message

text2 = 'jgnnq'

def creating_minus_shift_dict(shift):
	for k, v in origial_dict.items():
		if k in lower_alphabet:
			new_value = v - shift
			shift_dict[k] = new_value
		elif k in upper_alphabet:
			new_value = v - shift
			shift_dict[k] = new_value
	return(shift_dict)

def shifting_minus_dict():
	for k, v in shift_dict.items():
		shift_dict[k] = list_dict[v]
	return(shift_dict)





def uncipher_text(text, shift):
	shift_dict = creating_minus_shift_dict(shift)
	shift_dict = shifting_minus_dict()
	list_text = list(text)
	cipher_word = []
	for letter in list_text:
		if letter == ' ':
			cipher_word.append(' ')
		else:
			letter = shift_dict[letter]
			cipher_word.append(letter)
	cipher_word = ''.join(cipher_word)
	return(cipher_word)


def decrypt_message(text2):
	length_message = len(text2.split())
	list_text = list(text2)
	shift2 = 1
	while shift2 <= 26:
		possible_message = uncipher_text(text2, shift2)
		count = 0
		for word in possible_message:
			if is_word(word_list, word) is True:
				count += 1
			if count == length_message:
				return(possible_message)
			else:
				shift2 += 1





print(decrypt_message('jgnnq'))