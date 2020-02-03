# -*- coding: utf-8 -*-


# Python 3.4
# author: http://blog.dokenzy.com/
# date: 2015. 4. 8


# References
# http://www.imcore.net/encrypt-decrypt-aes256-c-objective-ios-iphone-ipad-php-java-android-perl-javascript/
# http://stackoverflow.com/questions/12562021/aes-decryption-padding-with-pkcs5-python
# http://stackoverflow.com/questions/12524994/encrypt-decrypt-using-pycrypto-aes-256
# http://www.di-mgt.com.au/cryptopad.html
# https://github.com/dlitz/pycrypto


import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS).encode()
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


def iv():
    return chr(0) * 16


class AESCipher(object):

    def __init__(self, key):
        self.key = key
        #self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, file ): #message
        file = file.encode()
        raw = pad(file)
        cipher = AES.new(self.key, AES.MODE_CBC, iv())
        enc = cipher.encrypt(raw)
        return base64.b64encode(enc).decode('utf-8')

    def decrypt(self, file):
        enc = base64.b64decode(file.read())
        cipher = AES.new(self.key, AES.MODE_CBC, iv())
        dec = cipher.decrypt(enc)
        return unpad(dec).decode('utf-8')
#-----------------------------above are methods

key = 'abcdefghijklmnopqrstuvwxyz123456'

#
_enc = 'gOXlygE+qxS+69zN5qC6eKJvMiEoDQtdoJb3zjT8f/E='


pick = input("Would you like to Encrypt or Decrypt a file?(1 - Enc 2 - Dec): ")
if(pick =="1"):
    fileOpen = input("Enter file name to encode: ");
    file = open(fileOpen)
    fileWrite = input("Enter a file to write to: ")
    fileWrite = open(fileWrite, 'w')
    enc = AESCipher(key).encrypt(file.read())
    fileWrite.writelines(enc)
    fileWrite.close()
elif(pick == "2"):
     fileOpen = input("Enter file name to decode: ");
     file = open(fileOpen)
     fileWrite = input("Enter a file to write to: ")
     fileWrite = open(fileWrite, 'w')
     dec = AESCipher(key).decrypt(file)
     fileWrite.write(dec)
     file.close()
     fileWrite.close()
else:
    print("Wrong input")




