import base64
from Crypto import Random
from Crypto.Cipher import AES

AKEY = 'mysixteenbytekey'
iv = 'what_a_cool_iv!!'

def decode(cipher):
    obj2 = AES.new(AKEY, AES.MODE_CFB, iv)
    return obj2.decrypt(base64.urlsafe_b64decode(cipher))

result = decode("5fMfiISsxcG4gKWAXwkL1Bu6zW26FlhG1613")

