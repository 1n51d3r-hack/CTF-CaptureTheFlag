key = 'encryptXOR'
code = 'UGFzc3dvcmQ6IHhvFzYMACEfBiAgIA=='
decode = ''
i = 0

for c in code:
    dec =  ord(c) ^ ord(key[i])
    i = (i+1)%len(key)

    decode = decode + chr(dec)

print decode