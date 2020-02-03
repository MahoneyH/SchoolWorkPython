from Crypto.Cipher import AES
import base64
import os

# the block size for the cipher object; must be 16 per FIPS-197
BLOCK_SIZE = 16

# the character used for padding--with a block cipher such as AES, the value
# you encrypt must be a multiple of BLOCK_SIZE in length.  This character is
# used to ensure that your value is always a multiple of BLOCK_SIZE
PADDING = '{'

# one-liner to sufficiently pad the text to be encrypted
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

# one-liners to encrypt/encode and decrypt/decode a string
# encrypt with AES, encode with base64
EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).decode("UTF-8").rstrip(PADDING)

#secret = "utV45S26510tvRtZ"
secret = "erikasthecoolest"

# create a cipher object using the random secret
cipher = AES.new(secret)

# encode a string
i = 0
while i ==0:
    UserInput = input("Would you like to encode or decode a message? (encode or decode)")
    if(UserInput =="encode"):
        encmsg = input("Enter Message to encode")
        encoded = EncodeAES(cipher, encmsg)
        print('Encrypted string:', encoded)
    elif(UserInput =="decode"):
        decmsg = input("Enter a message you would like to decode")
    # decode the encoded string
        decoded = DecodeAES(cipher, decmsg)
        print('Decrypted string:', decoded)
    cont = input("Continue to encode and decode?: 0 = yes, 1 = No")
    if(cont == "1"):
        i == 1
    elif(cont =="0"):
        i == 0


