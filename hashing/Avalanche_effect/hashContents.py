from cryptography.hazmat.primitives import hashes

hashFunct = ["MD5", "SHA256", "SHA384", "SHA512", "Blake2"] 

useHash = input("Hash Function (MD5, SHA256, SHA384, SHA512 and Blake2): ")
while useHash not in hashFunct:
    useHash = input("Hash Function (MD5, SHA256, SHA384, SHA512 and Blake2): ")

if useHash == "MD5":
    digest = hashes.Hash(hashes.MD5())

elif useHash == "SHA256":
    digest = hashes.Hash(hashes.SHA256())

elif useHash == "SHA384":
    digest = hashes.Hash(hashes.SHA384())

elif useHash == "SHA512":
    digest = hashes.Hash(hashes.SHA512())

elif useHash == "Blake2":
    digest = hashes.Hash(hashes.BLAKE2b(64))
    
fileToHash = input("File you want to encrypt:(txt file, doesn't need termination): ")
fileToHash += '.txt'

with open(fileToHash, 'r') as file:
    data = file.read().rstrip()
    digest.update(str.encode(data))

digestFinalize = digest.finalize()

#ONLY THIS IS DIFFERENT FROM THE OTHER CODE
#hashed_XXX_afterChange - delete last dot
with open("hashed_fileSHA512_afterChange.txt", 'w') as file:
    file.write(digestFinalize.hex())

print(digestFinalize.hex())