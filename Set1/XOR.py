import binascii

def XOR(hex_int_1, hex_int_2):
	# print hex_string_1 + '\n' + hex_string_2
	xor_string = str(hex(hex_int_1 ^ hex_int_2))
	return xor_string