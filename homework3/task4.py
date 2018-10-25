import sys
import crypt
import getpass
from hmac import compare_digest as compare_hash

#Check password guess, given a known hash.
def check_pass(guess, hash, count):
    if compare_hash(crypt.crypt(guess, hash), hash):
        found[hash] = (guess, count)


#Hashes from etc/shadow.txt file.
jons_hash = "$6$aBcDeF$qn4wyWpQKwjaKGr02tGUWKcFjl0p90b68.oaaJTFX87UzsSWIzq3ZoAEG0/xUQ1kcYTiHkKqye1Qat6vL4rMZ."
targ_hash = "aa.YVJDT1VruA"
tryn_hash = "$5$aAbBcCdD$TSZ4rpRmpbVDoas2FK97mHEZwXX"
arya_hash = "$1$bAc99821$noxC9VXXiMuA0IRfECCVA/"

#Empty dictionary for found passwords.
found = {}

#Keeptrackof howmany guesses are made.
count = 0

#Get args
filename = sys.argv[1]
mode = sys.argv[2]



#Intellegent generation of passwords from guess file.
if mode == "intellegent" : 
    with open(filename) as f:
        for line in f:
            mutations = list()

            mutations.append(line)

            #Add capital mutation
            mutations.append(mutations[0].capitalize())

            #Add capslock mutation
            mutations.append(mutations[0].upper())

            #Add numbers 1-10, 420, 66, 22, 99, 55, 69, 13, 777, 666, 
            for i in range(0,11):
                mutations.append(mutations[0] + str(i))
            mutations.append(mutations[0] + str(420))
            mutations.append(mutations[0] + str(66))
            mutations.append(mutations[0] + str(22))
            mutations.append(mutations[0] + str(99))
            mutations.append(mutations[0] + str(69))
            mutations.append(mutations[0] + str(13))
            mutations.append(mutations[0] + str(777))
            mutations.append(mutations[0] + str(666))

            #Reverse original word
            mutations.append(mutations[0][::-1])

            #Try each mutation
            for word in mutations:
                count += 1
                check_pass(word, jons_hash, count)
                check_pass(word, targ_hash, count)
                check_pass(word, tryn_hash, count)
                check_pass(word, arya_hash, count)

#Dumb parsing of guess file.
else:
    file = open(filename)
    lines = file.readlines()
    temp = [line[:-1] for line in lines]
    for i in temp:
        count += 1
        check_pass(i, jons_hash, count)
        check_pass(i, targ_hash, count)
        check_pass(i, tryn_hash, count)
        check_pass(i, arya_hash, count)

        
#Reveal found passwords.
print "{} password guesses were tried.".format(count)
print(found)


