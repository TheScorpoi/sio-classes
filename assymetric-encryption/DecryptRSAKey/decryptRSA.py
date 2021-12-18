from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

#Private Key
fileContainingPrivateKey = '../GenerateRSAKey/'
fileContainingPrivateKey += input("File containing the private key:(txt file, doesn't need termination or path): ")
fileContainingPrivateKey += '.txt'

#Content to Decrypt
contentToDecrypt = '../EncryptRSAKey/'
contentToDecrypt += input("File that contains content to decrypt:(txt file, doesn't need termination or path): ")
contentToDecrypt += '.txt'

#Save decrypted Content
decryptedContent = input("File to store decrypted message:(txt file, doesn't need termination or path): ")
decryptedContent += '.txt'

with open(contentToDecrypt, 'rb') as file:
    ciphertext = file.read().rstrip()

with open(fileContainingPrivateKey, "rb") as key_file:
    privatekey = serialization.load_pem_private_key(
        key_file.read(),
        password=b'mypassword',
    )

plaintext = privatekey.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

text_file = open(decryptedContent, 'w')
text_file.write(plaintext.decode())
text_file.close()

print("PlainText written with sucess!")