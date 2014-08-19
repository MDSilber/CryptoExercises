import itertools

def XOR(message, key):
	return bytes(message ^ key)
