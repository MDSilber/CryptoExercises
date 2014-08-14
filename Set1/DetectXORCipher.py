import SingleByteXORCipher as XORCipher

def find_cipher_in_list(cipher_list):
	best_match_string = ''
	best_match_score = 0
	index = 0
	for possible_cipher in cipher_list:
		possible_best_match = XORCipher.decode_single_character(possible_cipher)[0]
		if possible_best_match[1] > best_match_score:
			best_match_score = possible_best_match[1]
			best_match_string = str(possible_best_match[0])

	return (best_match_string, best_match_score)

# possible_ciphers = open('./4.txt', 'r').read().split()
# best_match = find_cipher_in_list(possible_ciphers)
# print str(best_match[0]).rstrip() + " : " + str(best_match[1])
