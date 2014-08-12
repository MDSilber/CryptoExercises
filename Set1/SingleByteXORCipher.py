import XOR

words_list = open('/usr/share/dict/words', 'r').read().split()

def score_string(string):
	number_of_valid_characters = 0
	for word in string.split():
		if word in words_list:
			number_of_valid_characters += len(word)

	return float(number_of_valid_characters)/float(len(string))


def decode(encoded_string):
	possible_decryptions = list()
 	for possible_key in xrange(0, 256):
 		message = ''
 		for index in xrange(0, len(encoded_string), 2):
 			decoded_value = int(encoded_string[index:index+2], 16) ^ possible_key 
 			message += chr(decoded_value)
		possible_decryptions.append(message)

	scored_decryptions = list()
	index = 1
	for possible_decryption in possible_decryptions:
		scored_decryptions.append((possible_decryption, score_string(possible_decryption)))

	scored_decryptions.sort(key=lambda tuple: tuple[1], reverse=True)

	print scored_decryptions[0][0]


decode('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')