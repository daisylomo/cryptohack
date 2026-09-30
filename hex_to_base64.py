import base64

bytes_out = bytes.fromhex('72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf')
base64_out = base64.b64encode(bytes_out)

print(base64_out)