import sys
import crypt
import getpass
from hmac import compare_digest as compare_hash

#Hashes from etc/shadow.txt file.
jons_hash = "$6$aBcDeF$qn4wyWpQKwjaKGr02tGUWKcFjl0p90b68.oaaJTFX87UzsSWIzq3ZoAEG0/xUQ1kcYTiHkKqye1Qat6vL4rMZ."
targ_hash = "aa.YVJDT1VruA"
tryn_hash = "$5$aAbBcCdD$TSZ4rpRmpbVDoas2FK97mHEZwXX"
arya_hash = "$1$bAc99821$noxC9VXXiMuA0IRfECCVA/"

#Empty dictionary for found passwords.
found = {}

#Keeptrackof howmany guesses are made.
count = 0

#Check password guess, given a known hash.
def check_pass(guess, hash):
    print(guess)
    if compare_hash(crypt.crypt(guess, hash), hash):
        found[hash] = guess
        
check_pass("GameOfThrones", jons_hash)
check_pass("GameOfThronesRulez", targ_hash)


