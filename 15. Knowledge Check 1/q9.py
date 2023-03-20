def encrypt(s):
    return ''.join(chr(ord(c) + 10) for c in s)

def decrypt(s):
    return ''.join(chr(ord(c) - 10) for c in s)

string = 'S}kkm*Xo\x81~yx'
print(decrypt(string))
