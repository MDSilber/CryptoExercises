#words_list = open('/usr/share/dict/words', 'r').read().split()

import string

def score_string(cipher_string):
    number_of_valid_characters = 0

    for char in cipher_string:
    	if char in 'aeioutsrnmchg ':
    		number_of_valid_characters += 2
        elif char in (string.letters + '1234567890 '):
            number_of_valid_characters += 1

    return number_of_valid_characters

#	for word in string.split():
#		if word in words_list:
#			number_of_valid_characters += len(word)

#	return float(number_of_valid_characters)/float(len(string))
