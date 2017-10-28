import binascii
import base64
hexa = input("Enter a hexadecimal value: ")
bina = binascii.unhexlify(hexa)
Base64 = base64.b64encode(bina)
print(Base64)
