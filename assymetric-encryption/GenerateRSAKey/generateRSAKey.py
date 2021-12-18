from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

keySize = int(input("Key size (1024, 2048, 3072 and 4096): "))
privateFile = input("Name of the file to store the private key(dont need to put termination): ")
publicFile = input("Name of the file to store the public key(dont need to put termination): ")

privateFile += ".txt"
publicFile += ".txt"

#private key serialization
private_key = rsa.generate_private_key(
	public_exponent=65537,
	key_size=keySize,
)

#without serialization print an object
print(private_key)

public_key = private_key.public_key()

#serialize private_key
private_key = private_key.private_bytes(
	encoding=serialization.Encoding.PEM,
	format=serialization.PrivateFormat.PKCS8,
	encryption_algorithm=serialization.BestAvailableEncryption(b'mypassword')
)


print("PRIVATE KEY")
print(private_key)


text_file = open(privateFile, 'wb')
text_file.write(private_key)
text_file.close()

#serialize public key
public_key = public_key.public_bytes(
	encoding=serialization.Encoding.PEM,
	format=serialization.PublicFormat.SubjectPublicKeyInfo
)

text_file = open(publicFile, 'wb')
text_file.write(public_key)
text_file.close()

print("PUBLIC KEY")
print(public_key)
