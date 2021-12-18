import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes



file = input("Nome do ficheiro a encriptar: ")
storeFile = input("Nome do folder para guardar o file: ")
cryptAlg = input("Nome do encryption algorithm: ")

if(cryptAlg == "AES"):
	key = os.urandom(32)
	iv = os.urandom(16)
	cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
elif(cryptAlg == "ChaCha20"):
	nonce = os.urandom(16)
	algorithm = algorithms.ChaCha20(bytes(32), nonce)
	cipher = Cipher(algorithm, mode=None)
else:
	print("Nenhum método de encriptacao pronto para este programa com esse nome")
	exit(0)
	
encryptor = cipher.encryptor()

f = open(file);
msg = f.read().encode()

padder = padding.PKCS7(128).padder()
padded_data = padder.update(msg)
padded_data += padder.finalize()

ct = encryptor.update(padded_data) + encryptor.finalize()
print(ct)

decryptor = cipher.decryptor()
decryptor.update(ct) + decryptor.finalize()

unpadder = padding.PKCS7(128).unpadder()
data = unpadder.update(padded_data)
data += unpadder.finalize()

print(data.decode())
