import hashlib

key = '0)%C.,?4X*:2"$-&;5?XS'

m = hashlib.md5()
m.update(key)

print 'flag{' + m.hexdigest() + '}'