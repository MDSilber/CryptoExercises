import DetectXORCipher as XORCipher

def binary_for_string(string1):
	string_binary = ''.join(format(ord(c), '08b') for c in string1)
	return string_binary

def hamming_distance(string_1_binary, string_2_binary):
	distance = 0

	for i in xrange(len(string_1_binary)):
		if string_1_binary[i] != string_2_binary[i]:
			distance += 1

	return distance

def find_key_length(encrypted_string):
	key_length = 0
	min_hamming_distance = float("inf")
	binary_string = binary_for_string(encrypted_string)

	for i in xrange(2, 40):
		substring_1 = binary_string[: 8*i]
		substring_2 = binary_string[8*i:16*i]

		ham_distance = hamming_distance(substring_1, substring_2)

		if ham_distance < min_hamming_distance:
			min_hamming_distance = ham_distance
			key_length = i

	return key_length

def chunk_string_into_blocks(string_to_be_chunked, length):
	return [string_to_be_chunked[x:x+length] for x in xrange(0, len(string_to_be_chunked), length)]

def encoded_transposed_chunks(chunks, length):
	# start with array of empty strings
	transposed_chunks = ['' for i in xrange(0, length)]

	for i in xrange(0, length):
		for chunk in chunks:
			current_string = str(transposed_chunks[i])
			current_string += str(chunk[i])
			transposed_chunks[i] = current_string

	return transposed_chunks


# encoded_string = open('./6.txt', 'r').read()
# key_length = find_key_length(encoded_string)
# encoded_binary_chunks = chunk_string_into_blocks(binary_for_string(encoded_string), key_length)
# transposed_chunks = encoded_transposed_chunks(encoded_binary_chunks, key_length)
