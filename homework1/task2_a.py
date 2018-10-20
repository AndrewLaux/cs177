
#Task 2 - (a) find corresponding plaintext.
ciphertext = b'KHAQWVTACPFVCMGCECVCRCTVVQUGGJQYKVYQTMUVJGHKTUVVJKPIAQWJCXGQPAQWTJCPFUKUCPQPYQTMKPIECV'

for K in range(0 , 26): 
    M = [chr(((i - 65) + K) % 26 + 65) for i in ciphertext]
    F = ''.join(M)
    print(F)






