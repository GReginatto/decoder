import base64

base64_rsa_key_password = "TcIHoIbSS80pEl05rbsXGQRk8Kolm8al98NnzTZZTfE="
base64_message = "3hi1zSHKwj8ch/S2hm4TD1DFGcNuiWNu+6ywRwv0UKLngDQ/H+CpunJOVuDoTnMt"

binary_rsa_key_password = base64.b64decode(base64_rsa_key_password)
hexadecimal_rsa_key_password = binary_rsa_key_password.hex()

binary_message = base64.b64decode(base64_message)
hexadecimal_message = binary_message.hex()

print("SHA-256 Encrypted Key =", hexadecimal_rsa_key_password)
print("Decoded Base64 Message =", hexadecimal_message)
