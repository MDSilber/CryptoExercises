import XOR
import ScoreString

def decode_single_character(encoded_string):
	possible_decryptions = list()
 	for possible_key in xrange(0, 256):
 		message = ''
 		for index in xrange(0, len(encoded_string), 2):
 			decoded_value = str(XOR.XOR(int(encoded_string[index:index+2], 16), possible_key))
 			message += chr(int(decoded_value, 16))
		possible_decryptions.append(message)

	scored_decryptions = list()
	index = 1
	for possible_decryption in possible_decryptions:
		scored_decryptions.append((possible_decryption, ScoreString.score_string(possible_decryption)))

	scored_decryptions.sort(key=lambda tuple: tuple[1], reverse=True)
	return scored_decryptions

# print decode_single_character('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')[0]
