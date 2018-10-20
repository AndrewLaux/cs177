from Crypto.Cipher import AES
import binascii
import sys
import struct

key = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
plaintext = b'\x10\x04\x20\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
key_int = int.from_bytes(key, 'big')

for i in range(0,600):
    key_int += 1
    key = key_int.to_bytes(16, 'big')
    encryption = AES.new(key, AES.MODE_ECB)
    ciphertext = encryption.encrypt(plaintext)
    if(ciphertext[15] == 0): 
        print(binascii.hexlify(ciphertext))
        print(binascii.hexlify(key))
        print("On iteration: " + str(i))




