import sys
import crypt

if len(sys.argv) != 2:
    print "Usage: {} password salt".format(sys.argv[0])
else:
    password = sys.argv[1]
    salt = "$6$aBcDeF$qn4wyWpQKwjaKGr02tGUWKcFjl0p90b68.oaaJTFX87UzsSWIzq3ZoAEG0/xUQ1kcYTiHkKqye1Qat6vL4rMZ."

    e_pass = crypt.crypt(password, salt)
    print(e_pass)