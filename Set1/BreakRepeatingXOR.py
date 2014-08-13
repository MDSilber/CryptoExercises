def hamming_distance(string1, string2):
	string_1_binary = ''.join(format(ord(c), '08b') for c in string1)
	string_2_binary = ''.join(format(ord(c), '08b') for c in string2)
	distance = 0
	
	for i in xrange(len(string_1_binary)):
		if string_1_binary[i] != string_2_binary[i]:
			distance += 1

	return distance

def decrypt_string(encrypted_string):
	for i in xrange(2, 40):
		print i
	
encoded_string = open('./6.txt', 'r').read()