from Crypto.Cipher import AES
import binascii
import sys
import struct

key = b'\x10\x04\x20\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
plaintext = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
encryption = AES.new(key, AES.MODE_ECB)
plaintext_int = int.from_bytes(plaintext, 'big')

for i in range(0,600):
    plaintext_int += 1
    plaintext = plaintext_int.to_bytes(16, 'big')
    ciphertext = encryption.encrypt(plaintext)
    if(ciphertext[15] == 0): 
        print(binascii.hexlify(ciphertext))
        print(binascii.hexlify(plaintext))
        print("On iteration: " + str(i))








