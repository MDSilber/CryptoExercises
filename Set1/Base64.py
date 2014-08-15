import binascii
import base64

def base_64_to_hex(base_64_string):
	return base64.decodestring(base_64_string).encode('hex')

def hex_to_base_64(hex_string):
	return base64.encodestring(hex_string.decode('hex'))

# print hex_to_base_64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')
