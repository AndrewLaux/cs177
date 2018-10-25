import sys
import crypt
import getpass
from hmac import compare_digest as compare_hash

#Check password guess, given a known hash.
def check_pass(guess, hash):
    if compare_hash(crypt.crypt(guess, hash), hash):
        found[hash] = guess
        println(guess)

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
    pass

#Dumb parsing of guess file.
else:
    file = open(filename)
    lines = file.readlines()
    for i in lines:
        count += 1
        check_pass(i, jons_hash)
        check_pass(i, targ_hash)
        check_pass(i, tryn_hash)
        check_pass(i, arya_hash)

        
#Reveal found passwords.
print "{} password guesses were tried.".format(count)
print(found)


