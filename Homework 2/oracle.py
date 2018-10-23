# CS177 -- padding oracle attacks This code is (unfortunately) meant
# to be run with Python 2.7.10 on the CSIL cluster
# machines. Unfortunately, cryptography libraries are not available
# for Python3 at present, it would seem.
from Crypto.Cipher import AES
import binascii
import sys
import copy

def check_enc(text):
    nl = len(text)
    val = int(binascii.hexlify(text[-1]), 16)
    if val == 0 or val > 16:
        return False

    for i in range(1,val+1):
        if (int(binascii.hexlify(text[nl-i]), 16) != val):
            return False
    return True
                                 
def PadOracle(ciphertext):
    if len(ciphertext) % 16 != 0:
        return False
    
    tkey = 'Sixteen byte key'

    ivd = ciphertext[:AES.block_size]
    dc = AES.new(tkey, AES.MODE_CBC, ivd)
    ptext = dc.decrypt(ciphertext[AES.block_size:])

    return check_enc(ptext)


# Padding-oracle attack comes here

if len(sys.argv) > 1:
    myfile = open(sys.argv[1], "r")
    ctext=myfile.read()
    myfile.close()

    # complete from here. The ciphertext is now (hopefull) stored in
    # ctext as a string. Individual symbols can be accessed as
    # ord(ctext[i]). Some more hints will be given on the Piazza
    # page.

    def ChangeByte(text, pos, byte):
        if (pos >= len(text) or len(byte) != 1):
            print("bad args")
        else:
            text[pos] = byte

    def IncreaseByte(byte):
        a = ord(byte)
        a = (a + 1) % 256
        return chr(a)


    def StageBlocksForCheck(text, block_index):
        if block_index >= len(text)/16:
            print("bad block index")
        elif block_index == 0:
            print("Don't need to check the IV")
        else:
            start = (block_index - 1) * 16 
            end = start + 32
            a = text[start:end]
            strng = "".join(a)
            return strng

    #Change input from string to list.
    textlist = list(ctext)
    ciphertext = copy.deepcopy(textlist)
    IV = textlist[0:16]
    plainlist = [chr(0) for i in range(0,len(ctext))]
    blist = [chr(0) for i in range(0, len(ctext))]
    
    

    for i in reversed(range(1, len(ctext)/16)):
        for j in reversed(range(0,16)):
            pos = (i*16) + j
            k = 16 - j
            if k == 1:
                byte = ciphertext[pos-16]
                byte = IncreaseByte(byte)
                ChangeByte(textlist, pos-16, byte)
                found = PadOracle(StageBlocksForCheck(textlist, i))

                #Find correct modification in cipher text for last byte.
                while found == False:
                    byte = IncreaseByte(byte) 
                    ChangeByte(textlist, pos-16, byte)
                    found = PadOracle(StageBlocksForCheck(textlist, i))

                #Check for false positive    
                preceding = ciphertext[pos-17]
                preceding = IncreaseByte(preceding)
                ChangeByte(textlist, pos-17, preceding)
                found = PadOracle(StageBlocksForCheck(textlist, i))
                
                #Continue looking for the true value in B.
                while found == False:
                    byte = IncreaseByte(byte)
                    ChangeByte(textlist, pos-16, byte)
                    found = PadOracle(StageBlocksForCheck(textlist, i))

                #Found the right modification, get plaintext.
                Y = ord(byte)
                B = Y^k
                blist[pos] = chr(B)
                y = ord(ciphertext[pos-16])
                P = chr(y^B)
                plainlist[pos] = P

            #For preceding bytes of block.
            else:
                for r in range(0,k-1):
                    pad_pos = ((i*16)+15) - r
                    textlist[pad_pos-16]=chr(ord(blist[pad_pos])^k) 

                found = PadOracle(StageBlocksForCheck(textlist, i))
                byte = ciphertext[pos-16]
              
                while found == False:
                    byte = IncreaseByte(byte)
                    ChangeByte(textlist, pos-16, byte)
                    found = PadOracle(StageBlocksForCheck(textlist, i)) 

                Y = ord(byte)
                B = Y^k
                blist[pos] = chr(B)
                y = ord(ciphertext[pos-16])
                P = chr(y^B)
                plainlist[pos] = P

    #Append IV to Plaintext
    for i in range(0, 16):
        plainlist[i] = IV[i]

    #Concatenate plaintext
    plaintext = "".join(plainlist)
    print(plaintext)

            
                

# end completing here, leave rest unchanged.
else:
    print("You need to specify a file!")
    
