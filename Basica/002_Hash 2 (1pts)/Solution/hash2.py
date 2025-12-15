import hashlib

key = "AMoreSecureHashFunction"

m = hashlib.sha256()
m.update(key)

m2 = hashlib.md5()
m2.update(m.hexdigest())

print 'flag{' + m2.hexdigest() + '}'