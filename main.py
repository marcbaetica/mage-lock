import mmh3


# def get_unsigned(number, bits=32):
def get_unsigned(num, bits=8):
    supported_bits_size = [8, 16, 32, 64, 128]
    if bits not in supported_bits_size:
        raise ValueError(f'Bits value has to be one of {supported_bits_size}.')
    mask = b'0x' + b'F' * int(bits/4)
    print(mask)
    print(type(mask))
    print(chr(mask))
    print(b'F'*4)


hashed = mmh3.hash(b'lala')
print(hashed)
print(hashed & 0xFFFFFFFF)

num = -1
print(num)
print(num & 0xFF)
print(num & 0xFFFF)

print(b'0x')
print(b'F' * 4)
print(b'F' + b'F')
get_unsigned(num)

