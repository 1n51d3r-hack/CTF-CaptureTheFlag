import hashlib
import base64

infile = open('Basic/base64.txt', 'r')

for line in infile:
    base = base64.b64decode(line)
    print base

infile.close()