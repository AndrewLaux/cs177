from Crypto.Cipher import AES
import binascii
import sys
import struct

key = b'\x10\x04\x20\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
plaintext = b'\x10\x04\x20\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
encryption = AES.new(key, AES.MODE_ECB)
ciphertext = encryption.encrypt(plaintext)
print(binascii.hexlify(ciphertext))



