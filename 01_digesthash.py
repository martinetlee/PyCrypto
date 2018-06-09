import nacl.encoding
import nacl.hash

# Practice 1
# message digest using hash function


###################
# Sender Side
###################

HASHER = nacl.hash.sha256
msg = "Here are some msg that is supposedly very long".encode('raw_unicode_escape')

digest = HASHER(msg, encoder=nacl.encoding.RawEncoder)
## What is encoding used for?
#

print("Msg : ",nacl.encoding.RawEncoder.encode(msg))
print("Digest : ", digest)

###################
# Receiver Side
###################


msg = "This is an altered message, seriously?".encode('raw_unicode_escape')
digest = HASHER(nacl.encoding.RawEncoder.encode(msg), encoder=nacl.encoding.RawEncoder)


print("Msg : ",nacl.encoding.RawEncoder.encode(msg))
print("Digest : ", digest)