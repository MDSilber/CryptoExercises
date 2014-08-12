import binascii

def XOR(hex_string_1, hex_string_2):
	return str(hex(int(hex_string_1, 16) ^ int(hex_string_2, 16)))