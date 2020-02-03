from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
import base64


def generate_keys():
    # RSA modulus length must be a multiple of 256 and >= 1024
    # modulus_length = 256 * 4  # use larger value in production
    # privatekey = RSA.generate(modulus_length, Random.new().read)
    key = RSA.generate(2048)
    privatekey = key.exportKey()
    file_out = open("private.pem", "w")
   # privatekey.write(str(privatekey.exportKey(), "utf-8"))
    file_out.write(privatekey)

    publickey = key.publickey().exportKey()
    #publickey.write(str(publickey.exportKey(), "UTF-8"))
    file_out = open("receiver.pem", "w")
    file_out.write(publickey)
    # publickey = privatekey.publickey()
    return privatekey, publickey


def encrypt_message(a_message, publickey):
    encrypted_msg = publickey.encrypt(a_message, 32)[0]
    encoded_encrypted_msg = base64.b64encode(encrypted_msg)  # base64 encoded strings are database friendly
    return encoded_encrypted_msg


def decrypt_message(encoded_encrypted_msg, privatekey):
    decoded_encrypted_msg = base64.b64decode(encoded_encrypted_msg)
    decoded_decrypted_msg = privatekey.decrypt(decoded_encrypted_msg)
    return decoded_decrypted_msg


# BEGIN

a_message = "The quick brown fox jumped over the lazy dog"
recipient_key = RSA.importKey(open("receiver.pem").read()) #receiver is a pub key
encrypted_msg = encrypt_message(a_message.encode("utf-8"), recipient_key)
file_out = open("encrypted_data.txt", "w")
#file_out.write(str(encrypted_msg, "utf-8"))
session_key = get_random_bytes(16)

# Encrypt session key with public rsa key
cipher_rsa = PKCS1_OAEP.new(recipient_key)
enc_session_key = cipher_rsa.encrypt(session_key)

# Decrypt session key with the private rsa key
private_key = RSA.importKey(open("private.pem").read())
file_in = open("encrypted_data.txt", "r")
cipher_rsa = PKCS1_OAEP.new(private_key)
session_key = cipher_rsa.decrypt(enc_session_key)


# privatekey, publickey = generate_keys()
# encrypted_msg = encrypt_message(a_message.encode("utf-8"), publickey)
# decrypted_msg = decrypt_message(encrypted_msg, privatekey)

# print("%s - (%d)" % (privatekey.exportKey(), len(privatekey.exportKey())))
# print("%s - (%d)" % (publickey.exportKey(), len(publickey.exportKey())))
# print(" Original content: %s - (%d)" % (a_message, len(a_message)))
# print("Encrypted message: %s - (%d)" % (encrypted_msg, len(encrypted_msg)))
# print("Decrypted message: %s - (%d)" % (decrypted_msg, len(decrypted_msg)))

