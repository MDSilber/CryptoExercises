import binascii
import base64

def base_64_to_hex(base_64_string):
	return base64.decodestring(base_64_string).encode('hex')

def hex_to_base_64(hex_string):
	return base64.encodestring(hex_string.decode('hex'))

def base_64_to_bytes(base_64_string):
	return base64.b64decode(base_64_string)

def bytes_to_base_64(byte_string):
	return base64.b64encode(byte_string).decode()

def hex_to_bytes(hex_string):
	return hex_string.encode()

def str_to_bytes(text):
	decoded_text = text.decode("utf-8")
	return decoded_text
