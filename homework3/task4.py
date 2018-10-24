import sys
import crypt

if len(sys.argv) != 2:
    print "Usage: {} password salt".format(sys.argv[0])
else:
    password = sys.argv[1]
    salt = "$6$aA349808Abcd$"

    e_pass = crypt.crypt(password, salt)
    print "Password: {} Salt: {} Hash: {}".format(password, salt, e_pass)