import hashlib

#Para obtener la key, utilizar la web https://crackstation.net/

key = "ADMINISTRATOR"

m = hashlib.md5()
m.update(key)

print 'flag{' + m.hexdigest() + '}'