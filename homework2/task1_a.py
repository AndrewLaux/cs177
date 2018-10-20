from os import urandom
from Crypto.Cipher import AES
from Crypto.Util import Counter
import binascii

plaintext_m1 = "Nothing to report."
plaintext_m3 = "Noyhin6 to report."


#generate random key
encrypt_key = urandom(16)

# create counter object using a random, 16-byte long IV
iv = urandom(16)
ctr = Counter.new(128, initial_value=int(binascii.hexlify(iv), 16))

#create 'AES object'
cipher = AES.new(encrypt_key, AES.MODE_CTR, counter=ctr)

#create ciphertext
ciphertext = iv + cipher.encrypt(bytes(plaintext_m1, 'ascii'))

ctr = Counter.new(128, initial_value=int(binascii.hexlify(iv), 16))

#create 'AES object'
cipher = AES.new(encrypt_key, AES.MODE_CTR, counter=ctr)

ciphertext1 = iv + cipher.encrypt(bytes(plaintext_m3, 'ascii'))

#print ciphertext
print(binascii.hexlify(ciphertext))
print(binascii.hexlify(ciphertext1))