import Crypto
import Base64

def problem_1():
  print Base64.hex_to_base_64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')

def problem_2():
  decimal_xor = Crypto.XOR(0x1c0111001f010100061a024b53535009181c, 0x686974207468652062756c6c277320657965)
  print hex(int(decimal_xor))

def problem_3():
  ordered_possibilities = Crypto.brute_single_char_xor('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
  print ordered_possibilities[0]

def problem_4():
  possible_ciphers = open('./4.txt', 'r').read().split()
  best_match = Crypto.find_xor_cipher_in_list(possible_ciphers)
  print str(best_match[0]).rstrip() + " : " + str(best_match[1])

def problem_5():
  print Crypto.xor_encode('ICE', 'Burning \'em, if you ain\'t quick and nimble\nI go crazy when I hear a cymbal')

def problem_6():
  print "Test"
