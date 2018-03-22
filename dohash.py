#!/usr/bin/env python3

import hashlib

print('''{'md5','sha224', 'sha256', 'blake2s256',  'sha384','md5-sha1',  
 'sha1',  'whirlpool', 'ripemd160', 'sha512', 'blake2b512', 'md4'}
''')
hashtype=input('enter hash type:')
pas=str(input('enter your hash:'))
h=hashlib.new(hashtype)
pas=pas.encode('ascii')
h.update(pas)
cs=h.digest_size
ns=h.block_size
print('cracter namer:{}'.format(ns))
print('memoiry size:{}'.format(cs))
h=h.hexdigest()
print (h)
d=len(h)
print(d)
