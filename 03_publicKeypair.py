import nacl.utils

from nacl.encoding import HexEncoder
from nacl.public import PrivateKey, Box


# Practice 3
# Basics of public key cryptography
#   (1) Generating
#   (2) Encrypting
#   (3) Decrypting

"""

The Box class uses the given public and private (secret) keys to derive a shared key, 
which is used with the nonce given to encrypt the given messages and to decrypt the given ciphertexts.
The same shared key will be generated from both pairing of keys, 
so given two keypairs belonging to Alice (pkalice, skalice) and Bob (pkbob, skbob), 
the key derived from (pkalice, skbob) will equal that from (pkbob, skalice).

"""

# Generate a public / private key pair for Alice and Bob
## Alice
sk_A = PrivateKey.generate()
pk_A = sk_A.public_key

## Bob
sk_B = PrivateKey.generate()
pk_B = sk_B.public_key


#Hexify the public keys
pk_AHex = pk_A.encode(HexEncoder)
pk_BHex = pk_B.encode(HexEncoder)


# Sending data. From A to B

## Creating the box
ABox = Box(sk_A, pk_B)

## let the data be a byte array
msg = "Here is some data, password is as the following"
byte_msg = bytes(msg.encode())

## Encrypt the byte array data
cipherText = ABox.encrypt(byte_msg)



# Receiving data, on B's side

## Creating the box
BBox = Box(sk_B, pk_A)
recovered_bytearray = BBox.decrypt(cipherText)
recoveredText = recovered_bytearray.decode()

print("Recovered Text:", recoveredText)








