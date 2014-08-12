import binascii

def hex_to_base_64(hex_string):
	binary_string = binascii.unhexlify(hex_string)
	base_64_string = binascii.b2a_base64(binary_string)
	return base_64_string

#hex_to_base_64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')
