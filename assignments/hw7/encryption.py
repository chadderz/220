def encode():
    message = "hi"
    key = 0
    encrypt = ""
    for char in message:
        num = ord(char) + key
        encrypt += chr(num % 128)
    return encrypt