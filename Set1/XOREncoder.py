import XOR

def xor_key(length):
	key = ''
	for i in xrange(0, length):
		if i%3 == 0:
			key += 'I'
		elif i%3 == 1:
			key += 'C'
		else:
			key += 'E'

	return key

def xor_encode(message):
	key = xor_key(len(message))

	encoded_string = ''
	index = 0
	while index < len(message):
		encoded_char = XOR.XOR(ord(message[index]), ord(key[index]))
		encoded_string += format(int(encoded_char, 16), 'x'))
		index += 1

	return encoded_string

print int(xor_encode('Burning \'em, if you ain\'t quick and nimble\nI go crazy when I hear a cymbal'))
