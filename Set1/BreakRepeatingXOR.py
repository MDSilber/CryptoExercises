import SingleByteXORCipher as XORCipher
import Base64

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
	binary_string = binary_for_string(encrypted_string)
	key_lengths = {}

	for i in xrange(2, 40):
		substring_1 = binary_string[: 8*i]
		substring_2 = binary_string[8*i:16*i]

		key_lengths[i] = float((hamming_distance(substring_1, substring_2)))/float(i)

	return sorted(key_lengths.items(), key=lambda x: x[1])

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

def decode_transposed_chunks(chunks):
	return [XORCipher.decode_single_character(chunk)[0] for chunk in chunks]

def reconstruct_message_from_decoded_transposed_chunks(chunks):
	message = ''
	chunk_length = len(chunks[0])

	for i in xrange(0, chunk_length):
		for chunk in chunks:
			message += str(chunk[i])

	return message

def test_chunking(message):
	chunks = chunk_string_into_blocks(message, 4)
	transposed_chunks = encoded_transposed_chunks(chunks, 4)
	new_message = reconstruct_message_from_decoded_transposed_chunks(transposed_chunks)
	assert(message == new_message)
	print new_message

# running the code

encoded_string = open('./6.txt', 'r').read()
# print encoded_string
key_length = find_key_length(encoded_string)
print key_length
# encoded_chunks = chunk_string_into_blocks(binary_for_string(encoded_string), key_length)
# # print encoded_chunks
# transposed_chunks = encoded_transposed_chunks(encoded_chunks, key_length)
# # print transposed_chunks
# decoded_transposed_chunks = decode_transposed_chunks(transposed_chunks)
# #print decoded_transposed_chunks
# print reconstruct_message_from_decoded_transposed_chunks(decoded_transposed_chunks)
