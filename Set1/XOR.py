import binascii

def XOR(hex_string_1, hex_string_2):
	# print hex_string_1 + '\n' + hex_string_2
	xor_string = str(hex(int(hex_string_1, 16) ^ int(hex_string_2, 16)))
	return xor_string