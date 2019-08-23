import base64

encode_decode = input("Encode or Decode? ")

def encode():
    while True:
        message = input("What's the message? ")
        data = base64.b64encode(message.encode())
        if len(message) > 0:
            print(data)
            break
        else:
            print("error")
            break

def decode():
    while True:
        code = input("What is the code? ")
        data = base64.b64decode(code)
        if len(code) > 0:
            print(data)
            break
        else:
            print("error")
            break
            
if encode_decode.lower() == 'encode':
    encode()
else:
    decode()
