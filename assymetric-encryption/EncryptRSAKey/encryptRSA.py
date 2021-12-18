from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

#Message to encrypt
fileToEncrypt = input("File you want to encrypt:(txt file, doesn't need termination): ")
fileToEncrypt += '.txt'

with open(fileToEncrypt, 'r') as file:
    data = file.read().rstrip()

#Message encoded to bytes
message = str.encode(data)

#Public Key
fileContainingPublickKey = '../GenerateRSAKey/'
fileContainingPublickKey += input("File containing the publick key:(txt file, doesn't need termination or path): ")
fileContainingPublickKey += '.txt'

#New File Encrypted
newFileEncrypted = input("Name for the new encrypted file:(txt file, doesn't need termination): ")
newFileEncrypted += '.txt' 

public_key = open(fileContainingPublickKey, "rb")
public_key = public_key.read()
public_key = load_pem_public_key(public_key)

#encrypt with the public key
ciphertext = public_key.encrypt(
	message,
	padding.OAEP(
		mgf=padding.MGF1(algorithm=hashes.SHA256()),
		algorithm=hashes.SHA256(),
		label=None
    )
)


text_file = open(newFileEncrypted, 'wb')
text_file.write(ciphertext)
text_file.close()

print("Text written in new file!")
