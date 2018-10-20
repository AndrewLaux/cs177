
ciphertext = 0xFFBC1ADC607ACDDEAE7D837FA8123A3A9CFDD83A9CD55F15A8CD7F8CFA32A67B
ciphertext = hex(ciphertext)
print(int(ciphertext[32:34], 16))
y_prime = hex(int(ciphertext[32:34], 16) ^ 1 ^ 8)
print(y_prime)



