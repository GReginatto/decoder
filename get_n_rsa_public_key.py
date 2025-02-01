from Crypto.PublicKey import RSA
import base64

rsa_public_key_base64 = "MEwwDQYJKoZIhvcNAQEBBQADOwAwOAIxAKoX4TOcmaDzmdgY3F2frRY8hX1sDnWTnjK5kRgfZ04CxDH7F/1f//YZfnv1/KOG7QIDAQAB"

rsa_public_key_bytes = base64.b64decode(rsa_public_key_base64)
rsa_public_key = RSA.importKey(rsa_public_key_bytes)
n = rsa_public_key.n
e = rsa_public_key.e

print("n =", n)
print("e =", e)
