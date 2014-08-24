import Base64
import string

def XOR(message, key):
  return str(message ^ key)

def score_string(cipher_string):
    number_of_valid_characters = 0

    for char in cipher_string:
      if char in 'etaoinsrhldcu ':
        number_of_valid_characters += 2
      elif char in (string.letters + '1234567890 '):
        number_of_valid_characters += 1

    return number_of_valid_characters

def brute_single_char_xor(encoded_string):
  possible_decryptions = list()
  for possible_key in xrange(0, 256):
    message = ''
    for index in xrange(0, len(encoded_string), 2):
      decoded_value = XOR(int(encoded_string[index:index+2], 16), possible_key)
      message += chr(int(decoded_value))

    possible_decryptions.append(message)

  scored_decryptions = list()
  index = 1
  for possible_decryption in possible_decryptions:
    scored_decryptions.append((possible_decryption, score_string(possible_decryption)))

  scored_decryptions.sort(key=lambda tuple: tuple[1], reverse=True)
  return scored_decryptions

def find_xor_cipher_in_list(cipher_list):
  best_match_string = ''
  best_match_score = 0
  index = 0
  for possible_cipher in cipher_list:
    possible_best_match = brute_single_char_xor(possible_cipher)[0]
    if possible_best_match[1] > best_match_score:
      best_match_score = possible_best_match[1]
      best_match_string = str(possible_best_match[0])

  return (best_match_string, best_match_score)

def xor_key(key_base, message_length):
  key = ''

  for i in xrange(0, message_length):
    key += key_base[i % len(key_base)]

  return key

def xor_encode(key, message):
  key = xor_key(key, len(message))

  encoded_string = ''
  for i in xrange(0, len(message)):
    encoded_char = XOR(ord(message[i]), ord(key[i]))
    encoded_string += format(int(encoded_char), 'x')

  return encoded_string
